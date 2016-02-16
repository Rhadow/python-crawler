import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def _get_new_urls(page_url, soup):
    new_urls = set()
    parsed_url = urlparse(page_url)
    base_url = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
    links = soup.find_all(
      'a', href=re.compile(r'^/[a-zA-Z0-9_-]+(\?tab=repositories)?$'))
    for link in links:
        new_url = link['href']
        new_urls.add(urljoin(base_url, new_url))
    return new_urls


def _get_data(page_url, soup):
    if '?tab=repositories' not in page_url:
        return None
    total_stars = 0
    star_tags = soup.find_all('a', {'aria-label': 'Stargazers'})
    user_name = soup.find_all('div', class_='vcard-username')[0].getText()
    for star_tag in star_tags:
        stars = star_tag.getText().strip()
        total_stars += int(''.join(stars.split(',')))
    return '{0} has total of {1} stars'.format(user_name, total_stars)


def parse(page_url, html):
    if page_url is None or html is None:
        return None
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    new_urls = _get_new_urls(page_url, soup)
    data = _get_data(page_url, soup)
    return (new_urls, data)
