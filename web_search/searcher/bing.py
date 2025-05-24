import copy
import requests
from bs4 import BeautifulSoup

from web_search.searcher.comm_params import HEADERS

HOST = "cn.bing.com"
SEARCH_URL = "https://cn.bing.com/search?q={keyword}&form=ANNTH1"

def search_bing(keyword, cookie):
    if not cookie:
        raise ValueError("bing search: Cookie is required")
    # 构造 bing 搜索的 URL
    search_url = SEARCH_URL.format(keyword=keyword)
    
    # 设置请求头，模拟浏览器访问
    headers = copy.deepcopy(HEADERS)
    headers["Host"] = HOST
    headers["Cookie"] = cookie
    
    # 发送 GET 请求
    response = requests.get(search_url, headers=headers)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析 HTML 内容
        # open('bing.html', "w", encoding="utf-8").write(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 查找搜索结果，bing 搜索结果的标题通常在 <h3> 标签中，链接在 <a> 标签的 href 属性中
        results = soup.find_all("li", class_="b_algo")
        
        # 提取标题和链接
        search_results = []
        for r in results:
            logo = r.find("div", class_="rms_iac")
            website = r.find("div", class_="tptt")
            title = r.find("h2")
            link = title.find("a")
            content = r.find("div", class_="b_caption").get_text()
            if not content:
                continue
            details = content.split(" · ")
            date = ""
            try:
                # 需要将 2023年10月19日 格式化为 2023-10-19
                if len(details) >= 2:
                    date = details[0].replace("年", "-").replace("月", "-").replace("日", "")
            except Exception as e:
                raise e
            search_results.append({
                "logo": logo.get("data-src"),
                "website": website.get_text(),
                "title": title.get_text(),
                "link": link.get("href"),
                "detail": details[-1],
                "date": date
            })
        
        return search_results
    else:
        print(f"bing 搜索请求失败，状态码：{response.status_code}")
        return []