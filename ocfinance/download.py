import pandas as pd

from . import scraper

def download(url, start=None, end=None, **kwargs):
    """
    Downloads the data from the given URL and returns a pandas DataFrame.
    """
    CHECKONCHAIN_BASE_URL = "https://charts.checkonchain.com"
    CHAINEXPOSED_BASE_URL = "https://chainexposed.com"
    BITBO_BASE_URL = "https://charts.bitbo.io"
    WOOCHARTS_BASE_URL = "https://woocharts.com"
    CRYPTOQUANT_BASE_URL = "https://cryptoquant.com"
    BITCOINMAGAZINEPRO_BASE_URL = "https://www.bitcoinmagazinepro.com"

    data = pd.DataFrame()

    if url.startswith(CHECKONCHAIN_BASE_URL):
        data = scraper.checkonchain._download(url)
    elif url.startswith(CHAINEXPOSED_BASE_URL):
        data = scraper.chainexposed._download(url)
    elif url.startswith(BITBO_BASE_URL):
        data = scraper.bitbo._download(url)
    elif url.startswith(WOOCHARTS_BASE_URL):
        data = scraper.woocharts._download(url)
    elif url.startswith(CRYPTOQUANT_BASE_URL):
        data = scraper.cryptoquant._download(url, **kwargs)
    elif url.startswith(BITCOINMAGAZINEPRO_BASE_URL):
        data = scraper.bitcoinmagazinepro._download(url)
    else:
        raise ValueError("URL does not match any known source. Find the list of supported websites here: https://github.com/dhruvan2006/ocfinance/blob/main/README.md")
    
    return data
