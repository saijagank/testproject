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

    else:
        print("Received an error from the server, cannot print results", response.status_code)
