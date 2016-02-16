import requests


def download_html_content(url):
    if url is None:
        return None
    try:
        res = requests.get(url)
        if res.status_code == 404:
            return None
    except:
        return None
    return res.text
