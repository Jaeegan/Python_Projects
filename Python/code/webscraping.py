# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:10:51 2021

@author: Joshua
"""

import pandas as pd

# %%
import requests
from bs4 import BeautifulSoup

url = "https://www.guru99.com/reading-and-writing-files-in-python.html"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
print(soup)

table = soup.find("table")

headers = []

for column in table.find_all("th"):
    title = column.text.replace("\n", "")
    headers.append(title)

df = pd.DataFrame(columns=headers)

for row in table.find_all("tr")[1:]:
    data = row.find_all("td")
    row_data = [td.text.replace("\n", "") for td in data]
    length = len(df)
    df.loc[length] = row_data

df.to_csv("File Modes in Python.txt", index=False)

pd.read_csv("File Modes in Python")

# %%

import urllib.request

from bs4 import BeautifulSoup

repeat = int(input("Enter Number of repetitions: "))
linkpos = int(input("Enter Link Position to follow: "))

url = "http://py4e-data.dr-chuck.net/known_by_Miah.html"

for i in range(repeat):
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")
    # print(soup)

    urllist = list()
    tags = soup.find_all("a")
    for tag in tags:
        urllist.append(tag.get("href", None))
        # print(tag.attrs)
        # print(tag.contents)

    url = urllist[linkpos - 1]
    print(url)

# %%
# -*- coding: utf-8 -*-
"""
    Scrape tag value from xml url

Usage:
    ./moduleName.py

Author:
    Joshua Gan - 12.06.2023
"""

import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = "http://py4e-data.dr-chuck.net/comments_1599209.xml"

urlhand = urlopen(url).read()
tree = ET.fromstring(urlhand)

tags = tree.findall(".//count")

numlist = list()
for tag in tags:
    num = int(tag.text)
    numlist.append(num)

total = sum(numlist)
print(total)

# %%
# -*- coding: utf-8 -*-
"""
    Scrape value from json url

Usage:
    ./moduleName.py

Author:
    Joshua Gan - 12.06.2023
"""

import json
import ssl
import urllib.parse
import urllib.request

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.goggleapis.com/maps/api/geocode/json?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location:")
    if len(address) < 1:
        break

    params = dict()
    params["address"] = address
    if api_key is not False:
        params["key"] = api_key
    url = serviceurl + urllib.parse.urlencode(params)

    urlhand = urllib.request.urlopen(url, context=ctx).read().decode()
    # print(urlhand)

    data = json.loads(urlhand)
    for ele in data["results"]:
        pls_id = ele["place_id"]
        print(pls_id)
