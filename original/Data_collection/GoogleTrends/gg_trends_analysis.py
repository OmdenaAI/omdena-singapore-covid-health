import pandas as pd
import datetime      
import sys
import csv
from pytrends.request import TrendReq

def time_analysis(source, ts):
	figName = getFileName('figure', 'analysis_over_time_IN', source, ts)
	csvName = getFileName('CSV', 'analysis_over_time_IN', source, ts)
	df = pytrend.interest_over_time()
	df = df.drop(labels=['isPartial'],axis='columns')
	df.to_csv('./Results/CSVs/' + csvName, encoding='utf_8_sig')
	image = df.plot(title = source + ' searchs in 2020 on Google Trends India')
	fig = image.get_figure()
	fig.savefig('./Results/figs/' + figName)
	

def regional_analysis(source, ts):
	figName = getFileName('figure', 'analysis_regional_IN', source, ts)
	csvName = getFileName('CSV', 'analysis_regional_IN', source, ts)
	df = pytrend.interest_by_region(inc_low_vol = True)
	df.to_csv('./Results/CSVs/' + csvName, encoding='utf_8_sig')
	image = df.plot(title = source + ' searchs in 2020 on Google Trends India',figsize=(120, 30), kind ='bar')
	fig = image.get_figure()
	fig.savefig('./Results/figs/' + figName)


def suggestions_analysis(source, ts):
	figName = getFileName('figure', 'suggestions_IN', source, ts)
	csvName = getFileName('CSV', 'suggestions_IN', source, ts)
	keywords = pytrend.suggestions(keyword=source)
	df = pd.DataFrame(keywords)
	df.drop(columns='mid')
	df.to_csv('./Results/CSVs/' + csvName, encoding='utf_8_sig')


def related_topics_analysis(source, ts):
	figName = getFileName('figure', 'related_topics_IN', source, ts)
	csvName = getFileName('CSV', 'related_topics_IN', source, ts)
	#pytrend.build_payload(kw_list=[source], timeframe = 'today 3-m', geo = 'IN', gprop='')
	#pytrend.build_payload(kw_list= [source], timeframe = '2020-01-01 2020-05-31', geo = 'IN', gprop='')
	related_topics = pytrend.related_topics()
	with open('./Results/CSVs/' + csvName, 'w') as f:
		for key in related_topics.keys():
			f.write("%s,%s\n"%(key,related_topics[key]))


def related_queries_analysis(source, ts):
	figName = getFileName('figure', 'related_queries_IN', source, ts)
	csvName = getFileName('CSV', 'related_queries_IN', source, ts)
	#pytrend.build_payload(kw_list=[source], timeframe = 'today 3-m', geo = 'IN', gprop='')
	#pytrend.build_payload(kw_list= [source], timeframe = '2020-01-01 2020-05-31', geo = 'IN', gprop='')
	related_queries = pytrend.related_queries()
	with open('./Results/CSVs/' + csvName, 'w') as f:
		for key in related_queries.keys():
			f.write("%s,%s\n"%(key,related_queries[key]))


def getFileName(type, func, source, ts):
	if type == 'figure' :
		txt = type + '_' + func + '_' + source + '_{}.png'
	elif type == 'CSV' :
		txt = type + '_' + func + '_' + source + '_{}.csv'
	fileName  = txt.format(ts)
	return fileName

def Main(data, ts):
	global pytrend 
	pytrend = TrendReq()
	
	for word in data:
		print('\n' + word)
		pytrend.build_payload(kw_list= [word], timeframe = '2020-01-01 2020-05-31', geo = 'IN', gprop='')
		try:
			time_analysis(word, ts)
		except: # catch *all* exceptions
			e = sys.exc_info()[0]
			print( "Error during time analysis execution: %s" % e )
		else:
	  		print("Time analysis completed successfully") 
		try:
			regional_analysis(word, ts)
		except: # catch *all* exceptions
			e = sys.exc_info()[0]
			print( "Error during regional analysis execution: %s" % e )
		else:
	  		print("Regional analysis completed successfully")
		try:
			related_queries_analysis(word, ts)
		except: # catch *all* exceptions
			e = sys.exc_info()[0]
			print( "Error during related queries analysis execution: %s" % e )
		else:
	  		print("Related queries analysis completed successfully")
		try:
			related_topics_analysis(word, ts)
		except: # catch *all* exceptions
			e = sys.exc_info()[0]
			print( "Error during related topics analysis execution: %s" % e )
		else:
	  		print("Related topics analysis completed successfully")
		try:
			suggestions_analysis(word, ts)
		except: # catch *all* exceptions
			e = sys.exc_info()[0]
			print( "Error during suggestions analysis execution: %s" % e )
		else:
	  		print("Suggestions analysis completed successfully")
