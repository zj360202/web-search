import copy
import requests
from bs4 import BeautifulSoup

from web_search.searcher.comm_params import HEADERS

HOST = "www.baidu.com"
SEARCH_URL = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={keyword}"

def search_baidu(keyword):
    # 构造 bing 搜索的 URL
    search_url = SEARCH_URL.format(keyword=keyword)
    
    # 设置请求头，模拟浏览器访问
    headers = copy.deepcopy(HEADERS)
    headers["Host"] = HOST
    
    # 发送 GET 请求
    response = requests.get(search_url, headers=headers)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析 HTML 内容
        # open('bing.html', "w", encoding="utf-8").write(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 查找搜索结果，bing 搜索结果的标题通常在 <h3> 标签中，链接在 <a> 标签的 href 属性中
        results = soup.find_all("div", class_="c-container")
        
        # 提取标题和链接
        search_results = []
        for r in results:
            logo = r.find("img", class_="cos-avatar-img")
            website = r.find("span", class_="cosc-source-text")
            title = r.find("h3")
            if not title:
                continue
            link = title.find("a")
            cc = r.find("div", class_="c-color")
            if not cc:
                continue
            details = cc.findAll("span")
            if not logo or not website or not link or not details:
                continue
            try:
                # 需要将 2023年10月19日 格式化为 2023-10-19
                date = details[0].get_text().replace("年", "-").replace("月", "-").replace("日", "")
            except Exception as e:
                raise e
            # end try
            search_results.append({
                "logo": logo.get("src"),
                "website": website.get_text(),
                "title": title.get_text(),
                "link": link.get("href"),
                "detail": details[-1].get_text(),
                "date": date,
            })
        
        return search_results
    else:
        print(f"bing 搜索请求失败，状态码：{response.status_code}")
        return []