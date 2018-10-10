#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:03:34 2018

@author: alexis
"""

import requests;

from bs4 import BeautifulSoup;
import re;

websites=["https://www.reuters.com/finance/stocks/financial-highlights/LVMHtah.MI","https://www.reuters.com/finance/stocks/financial-highlights/DANO.PA","https://www.reuters.com/finance/stocks/financial-highlights/AIR.PA"]
Company=["LVMH","Danone","Airbus"];

for i,site in enumerate (websites):
    
    req=requests.get(site);
    html=req.text;
    soup = BeautifulSoup(html,"html.parser");


    Quarter_Ending = soup.find_all("td",text = re.compile("Dec-18"))[0].findNext("td").findNext("td").get_text();
    Price = soup.find_all("span",class_ = "nasdaqChangeHeader")[0].findNext("span").get_text()
    Percentage = soup.find_all("span",class_="neg")[0].get_text()
    PercentageSharesOwned = (soup.find_all("strong",text="% Shares Owned:")[0].findNext("td").get_text())
    DividendYieldCompany = (soup.find_all("td",text="Dividend Yield")[0].findNext("td").get_text())
    DividendYieldIndustry = (soup.find_all("td",text="Dividend Yield")[0].findNext("td").findNext("td").get_text())
    DividendYieldSector = (soup.find_all("td",text="Dividend Yield")[0].findNext("td").findNext("td").findNext("td").get_text())

    print("Pour {}, le quarter Ending est {}, le prix est {}, pourcentage {} et le purcentage SharedOwned:{}".format(Company[i],Quarter_Ending,Price,Percentage,PercentageSharesOwned))