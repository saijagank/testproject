import numpy as np
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as soup
from datetime import date, timedelta
import json



def request_webpage(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36',
               'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    session = requests.Session()
    request = session.get(url, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    response = session.get(url, headers=headers, timeout=5, cookies=cookies)

    return response


def main_daily(url,path):

    # Call function with url
    response = request_webpage(url)

    if response.status_code == 200:
        print("Success", response.status_code)
        print("\n")

        # html parser
        htmlContent = response.content
        page_soup = soup(htmlContent, 'html.parser')

        # read class from web page.
        containers = page_soup.findAll("a", {
            "class": "file file--mime-application-pdf file--application-pdf pdf-download-link"}, limit=1)

        # Define an empty string
        link = ""

        for i in containers:
            link += i.get('href')

        global filename2
        filename2 = path+'EQUITY_' + str(date.today()) + ".csv"

        # Call function with link
        response = request_webpage(link)
        if response.status_code == 200:
            print("Success", response.status_code)
            file = open(filename2, 'wb')
            file.write(response.content)
            file.close()
            print("File downloaded")
        else:
            print("Received an error from the server, cannot print results", response.status_code)

        # Reading file using pandas
        df_symbol2 = pd.read_csv(filename2)
        df_symbol2.columns = df_symbol2.columns.str.lstrip().str.replace(" ","_")

        df_symbol2_eq = df_symbol2[(df_symbol2["SERIES"].isin(["EQ"]))]

        sym_list = [sym for sym in df_symbol2_eq['SYMBOL']]

        # Find current date
        to_date = date.today()

        # change from_date variable as reqd; It is set to T-3 as of now
        from_date = date(date.today().year, date.today().month, date.today().day -3)

        for i in range(0,len(sym_list)):
        #for i in range(0,1):
            try:
                #df1 = stock_df(symbol = sym_list[i], from_date = from_date,to_date = to_date, series="EQ")
                #df = df._append(df1,ignore_index=True)
                stock_csv(symbol = sym_list[i], from_date = from_date,to_date = to_date, series="EQ",
                         output = r"C:\Users\ikundu\OneDrive - ICE Inc\Knowledge Transfer Sessions\Stock Exchange Data\data\{}".format(sym_list[i] + "_" + str(from_date) + "_" + str(to_date) +".csv"))
                print("{} data downloaded".format(sym_list[i]))
            except:
                file = open('nodata_log.txt', 'w')
                file.write("Oops! No data found for symbol {}. Skipping...\n".format(sym_list[i]))
                file.close()
                continue
    else:
        print("Received an error from the server, cannot print results", response.status_code)
