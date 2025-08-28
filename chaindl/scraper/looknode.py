from urllib.parse import urlparse

import pandas as pd

import requests
import json

def _download(url):
    parsed = urlparse(url)
    metric = parsed.query.split("=")[1]

    api = f"https://www.looknode.com/api/{metric}"
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
    df = df.set_index('Date')

    if not df.empty:
        v_columns = sorted([col for col in df.columns if col.startswith("v")], 
                        key=lambda x: int(x[1:]) if x[1:].isdigit() else 0)
        df = df[v_columns]

    return df