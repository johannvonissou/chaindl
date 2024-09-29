import requests

def _get_page_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text
