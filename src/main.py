import url_manager
import sys
from downloader import download_html_content
from parser import parse


def crawl(initial_user='Rhadow'):
    INITIAL_URL = 'https://github.com/{0}?tab=repositories'\
      .format(initial_user)
    urls = url_manager.UrlManager(INITIAL_URL)
    result = []
    counter = 0
    while urls.has_url() and counter <= 10:
        url_to_crawl = urls.get_url()
        print('{0} => Crawling {1}'.format(counter, url_to_crawl))
        html_content = download_html_content(url_to_crawl)
        if html_content is None:
            break
        new_urls, data = parse(url_to_crawl, html_content)
        urls.add_urls(new_urls)
        if data is not None:
            counter += 1
            result.append(data)

    print(result)

if __name__ == '__main__':
    initial_user = sys.argv[1]
    crawl(initial_user)
