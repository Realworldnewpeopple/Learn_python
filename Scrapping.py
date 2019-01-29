#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
r =urlopen('https://www.slashroot.in/curl-command-tutorial-linux-example-usage')
data=r.read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')
parse=soup.find_all('pre')
finaldata=[]
for i in parse:
    data1=i.contents
    finaldata.append(data1)
print("the final list of data is :"+ str(finaldata))




