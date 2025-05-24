import unittest
from web_search.parser.html_cleaner import HtmlCleaner

class TestHtmlCleaner(unittest.TestCase):
    def test_clean_html_removes_attributes(self):
        html = '''
        <div class="container" id="main">
            <p style="color: red;">Test content</p>
        </div>
        '''
        expected = '''
        <div>
            <p>Test content</p>
        </div>
        '''
        cleaned = HtmlCleaner.clean_html(html)
        # 移除空白字符后比较
        self.assertEqual(
            ''.join(cleaned.split()),
            ''.join(expected.split())
        )

    def test_clean_html_removes_scripts(self):
        html = '''
        <html>
            <head>
                <script src="test.js"></script>
                <script>console.log('test');</script>
            </head>
            <body>
                <div>Content</div>
            </body>
        </html>
        '''
        cleaned = HtmlCleaner.clean_html(html)
        self.assertNotIn('script', cleaned.lower())

    def test_clean_html_removes_styles(self):
        html = '''
        <html>
            <head>
                <style>body { color: red; }</style>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <div>Content</div>
            </body>
        </html>
        '''
        cleaned = HtmlCleaner.clean_html(html)
        self.assertNotIn('style', cleaned.lower())
        self.assertNotIn('link', cleaned.lower())

    def test_clean_html_preserves_content(self):
        html = '''
        <div class="test">
            <h1 id="title">Header</h1>
            <p class="content">Paragraph</p>
        </div>
        '''
        cleaned = HtmlCleaner.clean_html(html)
        self.assertIn('Header', cleaned)
        self.assertIn('Paragraph', cleaned)

if __name__ == '__main__':
    unittest.main()