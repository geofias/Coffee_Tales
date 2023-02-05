import requests as r
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url_precipitation = "https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation"
url_temperature = "https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature"

def Scraping_table(url):
    '''The function scrapes the countries average precipitation and temperature tables from Wikipedia'''
    
    response = r.get(url)

    response_text = response.text
    soup = BeautifulSoup(response_text, "html.parser")

    scraped_table = soup.table

    headers = scraped_table.find_all("th")
    headers = [header.text.strip() for header in headers]

    rows = []
    data_rows = scraped_table.find_all("tr")

    for row in data_rows:
        value = row.find_all("td")
        beautified_value = [dp.text.strip() for dp in value]
        if len(beautified_value) == 0:
            continue

        rows.append(beautified_value)

    df = pd.DataFrame(rows, columns=headers)
    return df

precipitation = Scraping_table(url_precipitation)

temperature = Scraping_table(url_temperature)
temperature.iloc[187:190:2, 0] = ["Norway", "Denmark"]

precipitation.to_csv("./cluster_tables/precipitation.csv", index=False)
temperature.to_csv("./cluster_tables/temperature.csv", index=False)