

# 完成页面爬取和解析
def crawl_and_parse(url, save_path: str = ""):
    response = requests.get(url)

    # 保存文件
    if save_path:
        # 基于url计算md5值
        md5 = hashlib.md5(url.encode("utf-8")).hexdigest()

        with open(os.path..join(save_path, md5 + ".html"), "w", encoding="utf-8") as f:
            f.write(response.text)
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all("div", class_="c-container")
    search_results = []
    for r in results:
        logo = r.find("img", class_="cos-avatar-img")
        website = r.find("span", class_="cosc-source-text")
        title = r.find("h3")
        if not title:
            continue