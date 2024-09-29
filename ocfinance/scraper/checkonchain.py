import re
import json

import requests
import pandas as pd
from bs4 import BeautifulSoup

def _download(url):
    content = get_page_content(url)
    soup = BeautifulSoup(content, 'html.parser')
    scripts = soup.find_all('script')

    dfs = extract_data_from_scripts(scripts)

    merged_df = pd.concat(dfs, axis=1, join='outer')
    return merged_df

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        raise ValueError(f"Error fetching the URL: {e}")
    
def extract_data_from_scripts(scripts):
    dfs = []
    for script in scripts:
        if script.string and 'Plotly.newPlot' in script.string:
            matches = re.findall(r'"name":\s*"([^"]*)"\s*,.*?"x":\s*(\[[^\]]*\])\s*,\s*"y":\s*(\[[^\]]*\])', script.string)
            for match in matches:
                name, x_data, y_data = match
                name = name.replace('\\u003c', '<').replace('\\u003e', '>')
                x = json.loads(x_data)
                y = json.loads(y_data)

                df = pd.DataFrame({ name: y }, index=pd.to_datetime(x).date)
                df.index.name = 'Date'
                df = df.loc[~df.index.duplicated(keep='first')] # TODO: Give user option to either choose drop dupes or take avg
                dfs.append(df)
    
    return dfs
