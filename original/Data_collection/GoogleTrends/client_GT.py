import datetime      
import sys
from gg_trends_analysis import Main
from pytrends.request import TrendReq

ts = int(datetime.datetime.now().timestamp())

with open('kw_list.txt', 'r') as f:
	liste1 = f.readlines()

with open('kw_list_2.txt', 'r') as f:
	liste2 = f.readlines()

Main(liste1, ts)

Main(liste2, ts)