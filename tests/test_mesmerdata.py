import pandas as pd
import pytest

from chaindl.scraper.mesmerdata import _download

@pytest.mark.parametrize("url, expected_columns", [
    (
        "https://www.mesmerdata.com/on-chain-charts/btc-block-tx-count-sum/",
        ["BTC-USD", "BTC Block Height", "BTC Tx Count Sum"]
    ),
    (
        "https://www.mesmerdata.com/on-chain-charts/btc-realized-profit-loss-tx-max-usd/",
        ["BTC-USD", "BTC Block Height", "BTC Realized Profit Tx Max", "BTC Realized Loss Tx Max"]
    )
])
def test_looknode_download(url, expected_columns):
    data = _download(url)

    assert isinstance(data, pd.DataFrame)
    assert isinstance(data.index, pd.DatetimeIndex)

    assert all(col in data.columns for col in expected_columns)