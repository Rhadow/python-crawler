import url_manager, downloader, parser

INITIAL_URL = 'http://www.google.com'

if __name__ == '__main__':
    urls = url_manager.UrlManager(INITIAL_URL)
