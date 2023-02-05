import requests as r
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url_precipitation = "https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation"

def Precipitation_table(url):
    '''The function scrapes the countries average precipitation table from Wikipedia'''
    
    response = r.get(url)

    precipitation_text = response.text
    soup = BeautifulSoup(precipitation_text, "html.parser")

    precipitation_table = soup.table

    headers = precipitation_table.find_all("th")
    headers = [header.text.strip() for header in headers]

    rows = []
    data_rows = precipitation_table.find_all("tr")

    for row in data_rows:
        value = row.find_all("td")
        beautified_value = [dp.text.strip() for dp in value]
        if len(beautified_value) == 0:
            continue

        rows.append(beautified_value)

    df = pd.DataFrame(rows, columns=headers)
    return df

precipitation = Precipitation_table(url_precipitation)
print(precipitation.info())
print(precipitation.head())