from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver

import pandas as pd

import json
import time

def _download(url, **kwargs):
    data = _intercept_network_requests(url, **kwargs)

    all_series = []
    
    for raw_col in data:
        raw_col_data = raw_col["cache"]["daily"]

        if len(raw_col_data) == 0:
            continue
            
        dates = pd.to_datetime([item[0] for item in raw_col_data], unit='ms').normalize()
        values = [item[1] for item in raw_col_data]
        series = pd.Series(values, index=dates, name=raw_col["label"])
        all_series.append(series)
    
    if all_series:
        df = pd.concat(all_series, axis=1)
        df.sort_index(inplace=True)

        return df
    else:
        return pd.DataFrame()

def _check_validity(driver):
    raw = driver.execute_script("return JSON.stringify(window.series_list);")
    data = json.loads(raw)

    correct_cols = len(data) - 6
    correct = 0

    for raw_col in data:
        if len(raw_col["cache"]["daily"]) > 0:
            correct += 1

            if correct == correct_cols:
                return True, data
        
    return False, None

def _intercept_network_requests(url, check_interval=0.5, timeout=30):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for compatibility
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    start_time = time.time()

    while time.time() - start_time < timeout:
        valid, data = _check_validity(driver)

        if valid:
            break

        time.sleep(check_interval)

    driver.quit()

    return data