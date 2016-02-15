import unittest, collections
from src.url_manager import UrlManager

class TestUrlManager(unittest.TestCase):
    def setUp(self):
        self.manager = UrlManager('www.google.com')

    def tearDown(self):
        self.manager = None

    def test_initial(self):
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.google.com']))

    def test_add_url(self):
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.google.com']))
        self.manager.add_url('www.facebook.com')
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.google.com', 'www.facebook.com']))
        self.manager.add_url('www.facebook.com')
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.google.com', 'www.facebook.com']))
        google_url = self.manager.get_url()
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.facebook.com']))
        self.manager.add_url('www.google.com')
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.facebook.com']))

    def test_add_urls(self):
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.google.com']))
        self.manager.add_urls(['www.facebook.com', 'www.twitter.com'])
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.google.com', 'www.facebook.com', 'www.twitter.com']))

    def test_get_url(self):
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.google.com']))
        self.assertEqual(self.manager.has_url(), True)
        google_url = self.manager.get_url()
        self.assertEqual(google_url, 'www.google.com')
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque([]))

    def test_has_url(self):
        self.assertEqual(self.manager.urls_to_crawl,\
            collections.deque(['www.google.com']))
        self.assertEqual(self.manager.has_url(), True)
        google_url = self.manager.get_url()
        self.assertEqual(self.manager.has_url(), False)

if __name__ == '__main__':
    url_manager_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestUrlManager)
    unittest.TextTestRunner(verbosity=2).run(url_manager_test_suite)
