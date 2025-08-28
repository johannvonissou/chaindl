from urllib.parse import urlparse, parse_qs

import pandas as pd

import requests

API_MAPPING = {
    "activeAddNum": "/api/getActiveAddNum",
    "ageOnSale": "/api/ageOnSale",
    "Ahr999": "/api/Ahr999",
    "ASOL": "/api/ASOL",
    "ASOPR": "/api/ASOPR",
    "balancedPrice": "/api/balancedPrice",
    "balGt0AddCnt": "/api/balGt0AddCnt",
    "balGt0p01AddCnt": "/api/balGt0p01AddCnt",
    "balGt0p1AddCnt": "/api/balGt0p1AddCnt",
    "balGt100AddCnt": "/api/balGt100AddCnt",
    "balGt10AddCnt": "/api/balGt10AddCnt",
    "balGt10kAddCnt": "/api/balGt10kAddCnt",
    "balGt1kAddCnt": "/api/balGt1kAddCnt",
    "bdd": "/api/bdd",
    "bFundingRateDetail": "/api/bFundingRateDetail",
    "binaryCDD": "/api/binaryCDD",
    "bOpenInterestDetail": "/api/bOpenInterestDetail",
    "BTCETFDetail": "/api/btcEtfDetail",
    "chipPriceDis10Per": "/api/chipPriceDis10Per",
    "chipPriceDis10PerShort": "/api/chipPriceDis10PerShort",
    "chipPriceDis5Per": "/api/chipPriceDis5Per",
    "chipPriceDis5PerLong": "/api/chipPriceDis5PerLong",
    "chipPriceDis5PerShort": "/api/chipPriceDis5PerShort",
    "CVDD": "/api/CVDD",
    "deltaTop": "/api/deltaTop",
    "exBalAll": "/api/exBalance2?ex=all",
    "exBalBinance": "/api/exBalance2?ex=binance",
    "exBalBitfinex": "/api/exBalance2?ex=bitfinex",
    "exBalBybit": "/api/exBalance2?ex=bybit",
    "exBalDeribit": "/api/exBalance2?ex=deribit",
    "exBalHuobi": "/api/exBalance2?ex=huobi",
    "exBalKucoin": "/api/exBalance2?ex=kucoin",
    "exBalOk": "/api/exBalance2?ex=ok",
    "exIn": "/api/exIn",
    "exInAll": "/api/exFlowIn2?ex=all",
    "exInBinance": "/api/exFlowIn2?ex=binance",
    "exInBitfinex": "/api/exFlowIn2?ex=bitfinex",
    "exInBybit": "/api/exFlowIn2?ex=bybit",
    "exInDeribit": "/api/exFlowIn2?ex=deribit",
    "exInHuobi": "/api/exFlowIn2?ex=huobi",
    "exInKucoin": "/api/exFlowIn2?ex=kucoin",
    "exInOk": "/api/exFlowIn2?ex=ok",
    "exNetAll": "/api/exNetFlow2?ex=all",
    "exNetBinance": "/api/exNetFlow2?ex=binance",
    "exNetBitfinex": "/api/exNetFlow2?ex=bitfinex",
    "exNetBybit": "/api/exNetFlow2?ex=bybit",
    "exNetDeribit": "/api/exNetFlow2?ex=deribit",
    "exNetHuobi": "/api/exNetFlow2?ex=huobi",
    "exNetKucoin": "/api/exNetFlow2?ex=kucoin",
    "exNetOk": "/api/exNetFlow2?ex=ok",
    "exOutAll": "/api/exFlowOut2?ex=all",
    "exOutBinance": "/api/exFlowOut2?ex=binance",
    "exOutBitfinex": "/api/exFlowOut2?ex=bitfinex",
    "exOutBybit": "/api/exFlowOut2?ex=bybit",
    "exOutDeribit": "/api/exFlowOut2?ex=deribit",
    "exOutHuobi": "/api/exFlowOut2?ex=huobi",
    "exOutKucoin": "/api/exFlowOut2?ex=kucoin",
    "exOutOk": "/api/exFlowOut2?ex=ok",
    "fearAndGreedy": "/api/fearAndGreedy",
    "hashRate": "/api/hashRate",
    "historyRetracement": "/api/historyRetracement",
    "holderPosChange": "/api/holderPosChange",
    "holdTime": "/api/holdTime",
    "lastActSup1d1w": "/api/lastActSup1d1w",
    "lastActSup1m3m": "/api/lastActSup1m3m",
    "lastActSup1y2y": "/api/lastActSup1y2y",
    "lastActSup24": "/api/lastActSup24",
    "lastActSup2y3y": "/api/lastActSup2y3y",
    "lastActSup3m6m": "/api/lastActSup3m6m",
    "lastActSup3y5y": "/api/lastActSup3y5y",
    "lastActSup5y7y": "/api/lastActSup5y7y",
    "lastActSup6m12m": "/api/lastActSup6m12m",
    "lastActSup7y10y": "/api/lastActSup7y10y",
    "lastActSupGt10y": "/api/lastActSupGt10y",
    "lthBehav": "/api/lthBehav",
    "lthCoins": "/api/lthCoins",
    "LTHMVRV": "/api/LTHMVRV",
    "LTHNUPL": "/api/LTHNUPL",
    "LTHPLRatio": "/api/LTHPLRatio",
    "lthPositionChange": "/api/lthPositionChange",
    "lthSopr": "/api/lth_sopr",
    "LTHSupLos": "/api/LTHSupLos",
    "LTHSupPro": "/api/LTHSupPro",
    "lthUndersell": "/api/lthUndersell",
    "macroFib": "/api/macroFib",
    "marketHealth": "/api/marketHealth",
    "mCapRealizedRatio": "/api/mCapRealizedRatio",
    "MSOL": "/api/MSOL",
    "newAddress": "/api/newAddress",
    "NUPL": "/api/NUPL",
    "perVolumeLos": "/api/perVolumeLos",
    "perVolumePro": "/api/perVolumePro",
    "PiCircle": "/api/getPiCircle",
    "puellMultiple": "/api/puellMultiple",
    "realCapHODL": "/api/realCapHODL",
    "realizedLos": "/api/realizedLos",
    "realizedPLRatio": "/api/realizedPLRatio",
    "realizedPro": "/api/realizedPro",
    "realizePrice": "/api/realizePrice",
    "realizeProLoss": "/api/realizeProLoss",
    "relativeUnreaLos": "/api/relativeUnreaLos",
    "relativeUnreaPro": "/api/relativeUnreaPro",
    "revSup1y": "/api/revSup1y",
    "revSup2y": "/api/revSup2y",
    "revSup3y": "/api/revSup3y",
    "revSup5y": "/api/revSup5y",
    "revSup7y": "/api/revSup7y",
    "rhodl": "/api/rhodl",
    "RPV": "/api/RPV",
    "s2f": "/api/s2f",
    "sixtyDaysRaise": "/api/sixtyDaysRaise",
    "SLRV": "/api/SLRV",
    "SOPD_ATH": "/api/SOPD_ATH",
    "SOPD_PER": "/api/SOPD_PER",
    "sopr": "/api/sopr",
    "sthCoins": "/api/sthCoins",
    "sthCostPrice": "/api/sthCostPrice",
    "sthCostPriceV2": "/api/sthCostPriceV2",
    "sthHolderPosChange": "/api/sthHolderPosChange",
    "STHMVRV": "/api/STHMVRV",
    "STHNUPL": "/api/STHNUPL",
    "STHPLRatio": "/api/STHPLRatio",
    "sthPositionChange": "/api/sthPositionChange",
    "sthSopr": "/api/sth_sopr",
    "STHSupLos": "/api/STHSupLos",
    "STHSupPro": "/api/STHSupPro",
    "sthTwoPrice": "/api/sthTwoPrice",
    "supBalGt100k": "/api/supBalGt100k",
    "supBalLt0p001": "/api/supBalLt0p001",
    "supBalLt0p01": "/api/supBalLt0p01",
    "supBalLt0p1": "/api/supBalLt0p1",
    "supBalLt1": "/api/supBalLt1",
    "supBalLt100k": "/api/supBalLt100k",
    "supHoldTimeGt2y": "/api/supHoldTimeGt2y",
    "supHoldTimeGt3y": "/api/supHoldTimeGt3y",
    "supHoldTimeGt5y": "/api/supHoldTimeGt5y",
    "supHoldTimeGt7y": "/api/supHoldTimeGt7y",
    "supLthSthRatio": "/api/supLthSthRatio",
    "supplyAdjCDD": "/api/supplyAdjCDD",
    "transVolumeLos": "/api/transVolumeLos",
    "transVolumePro": "/api/transVolumePro",
    "twoYearMultiply": "/api/twoYearMultiply",
    "uFundingRateDetail": "/api/uFundingRateDetail",
    "uOpenInterestDetail": "/api/uOpenInterestDetail",
    "URPD_ATH": "/api/URPD_ATH",
    "URPD_ATH_STH": "/api/URPD_ATH_STH",
    "URPD_PER": "/api/URPD_PER",
    "URPD_PER_STH": "/api/URPD_PER_STH",
    "valueClass10": "/api/valueClass10",
    "valueClass100": "/api/valueClass100",
    "valueClass1k": "/api/valueClass1k",
    "valueClassGt1k": "/api/valueClassGt1k",
    "y1hodl": "/api/y1hodl",
}

def _download(url):
    parsed = urlparse(url)
    metric = None

    if parsed.query:
        qs = parse_qs(parsed.query)
        if qs:
            first_key = next(iter(qs))
            vals = qs.get(first_key)
            if vals:
                metric = vals[0]

    if not metric:
        metric = url

    if metric not in API_MAPPING:
        available = ", ".join(sorted(API_MAPPING.keys()))
        raise KeyError(f"No API mapping found for id '{metric}'. Available ids ({len(API_MAPPING)}): {available}.")

    api_path = API_MAPPING[metric]

    if api_path.startswith("/api/"):
        api = f"https://www.looknode.com{api_path}"
    elif api_path.startswith("http://") or api_path.startswith("https://"):
        api = api_path
    else:
        api = f"https://www.looknode.com/api/{api_path.lstrip('/')}"

    response = requests.get(api)
    response.raise_for_status()

    _json = response.json()
    data = _json.get("data", [])

    processed_data = []
    for entry in data:
        date = pd.to_datetime(entry["t"], unit="ms").normalize()

        values = {}
        for key, value in entry.items():
            if key == "t":
                continue
            if key == "v":
                values["v1"] = value
            elif key.startswith("v") and key[1:].isdigit():
                values[key] = value

        row = {"Date": date}
        row.update(values)
        processed_data.append(row)

    df = pd.DataFrame(processed_data)

    if not df.empty:
        df = df.set_index('Date')
        v_columns = sorted(
            [col for col in df.columns if col.startswith("v")],
            key=lambda x: int(x[1:]) if x[1:].isdigit() else 0
        )
        df = df[v_columns]

    return df
