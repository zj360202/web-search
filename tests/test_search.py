import unittest
from web_search.search import WebSearch

class TestWebSearch(unittest.TestCase):
    def setUp(self):
        self.searcher = WebSearch()

    def test_search_returns_list(self):
        results = self.searcher.search("2024年高考报名时间")
        self.assertIsInstance(results, list)
        self.assertTrue(len(results) > 0)

    # def test_search_result_structure(self):
    #     results = self.searcher.search("test query")
    #     self.assertTrue(all(
    #         isinstance(result, dict) and
    #         'title' in result and
    #         'link' in result and
    #         'snippet' in result
    #         for result in results
    #     ))

    # def test_get_suggestions(self):
    #     suggestions = self.searcher.get_suggestions("test")
    #     self.assertIsInstance(suggestions, list)
    #     self.assertTrue(len(suggestions) > 0)
    #     self.assertTrue(all(isinstance(s, str) for s in suggestions))

if __name__ == '__main__':
    unittest.main()