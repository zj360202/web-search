from bs4 import BeautifulSoup
import re

class HtmlCleaner:
    """用于清理HTML内容的工具类，去除样式和不必要的属性。"""

    @staticmethod
    def clean_html(html_content: str) -> str:
        """清理HTML内容，只保留基本标签结构。

        Args:
            html_content (str): 原始HTML内容

        Returns:
            str: 清理后的HTML内容
        """
        # 预处理：移除JavaScript注释和CDATA标签
        html_content = re.sub(r'//.*?[\r\n]', '\n', html_content)  # 移除单行JavaScript注释
        html_content = re.sub(r'/\*.*?\*/', '', html_content, flags=re.DOTALL)  # 移除多行JavaScript注释
        html_content = re.sub(r'<!\[CDATA\[.*?\]\]>', '', html_content, flags=re.DOTALL)  # 移除CDATA标签

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 移除script、style和link标签
        for tag in soup.find_all(['script', 'style', 'link', 'meta', 'svg']):
            tag.decompose()

        for tag in soup.find_all(True):
            tag.attrs = {k: v for k, v in tag.attrs.items() if k in ['src']}

        # 从根节点开始清理
        cleaned_soup = soup.html
        if cleaned_soup is not None:
            return str(cleaned_soup)
        return ""

    @staticmethod
    def clean_html_file(input_file: str, output_file: str = None) -> str:
        """清理HTML文件，只保留基本标签结构。

        Args:
            input_file (str): 输入HTML文件路径
            output_file (str, optional): 输出HTML文件路径。如果不指定，则返回清理后的内容。

        Returns:
            str: 清理后的HTML内容
        """
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # 清理HTML内容
        html_content = html_content.replace("\n", "")
        cleaned_html = HtmlCleaner.clean_html(html_content)

        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_html)

# python web_search/parser/html_cleaner.py
# hc = HtmlCleaner()
# hc.clean_html_file("bing.html", "test_cleaned.html")