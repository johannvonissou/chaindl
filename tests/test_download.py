import pandas as pd
import pytest
from unittest.mock import patch
from ocfinance import download

mocked_data = {
    "checkonchain": pd.DataFrame({'data': [1, 2, 3]}),
    "chainexposed": pd.DataFrame({'data': [4, 5, 6]}),
    "bitbo": pd.DataFrame({'data': [7, 8, 9]}),
    "woocharts": pd.DataFrame({'data': [10, 11, 12]}),
    "cryptoquant": pd.DataFrame({'data': [13, 14, 15]}),
    "bitcoinmagazinepro": pd.DataFrame({'data': [16, 17, 18]})
}

@pytest.mark.parametrize("url, expected_data, provider", [
    ("https://charts.checkonchain.com/some_data", mocked_data["checkonchain"], "checkonchain"),
    ("https://chainexposed.com/some_data", mocked_data["chainexposed"], "chainexposed"),
    ("https://charts.bitbo.io/some_data", mocked_data["bitbo"], "bitbo"),
    ("https://woocharts.com/some_data", mocked_data["woocharts"], "woocharts"),
    ("https://cryptoquant.com/some_data", mocked_data["cryptoquant"], "cryptoquant"),
    ("https://www.bitcoinmagazinepro.com/some_data", mocked_data["bitcoinmagazinepro"], "bitcoinmagazinepro"),
])
def test_download_valid_urls(url, expected_data, provider):
    with patch(f'ocfinance.scraper.{provider}._download', return_value=expected_data):
        result = download(url)
        pd.testing.assert_frame_equal(result, expected_data)
    
def test_download_invalid_url():
    invalid_url = "https://unknownsource.com/some_data"
    with pytest.raises(ValueError, match="URL does not match any known source"):
        download(invalid_url)
