import collections


class UrlManager(object):
    def __init__(self, initial_url):
        self.urls_to_crawl = collections.deque([initial_url])
        self.crawled_urls = collections.deque([])

    def add_url(self, url):
        if url is None:
            return
        if url not in self.urls_to_crawl and url not in self.crawled_urls:
            self.urls_to_crawl.append(url)

    def get_url(self):
        try:
            url = self.urls_to_crawl.popleft()
            self.crawled_urls.append(url)
            return url
        except:
            return ''

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_url(url)

    def has_url(self):
        return len(self.urls_to_crawl) != 0
