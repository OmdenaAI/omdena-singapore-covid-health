import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
import json
import objectpath


with open("bddjson2.json") as datafile:    
	myData = json.load(datafile)

json_tree = objectpath.Tree(myData['data'])
result_tuple = tuple(json_tree.execute('$..caption'))

dataset = ""
for ite in result_tuple:
  dataset = dataset + ite

def create_word_cloud(string):
   maskArray = npy.array(Image.open("pngwave.png"))
   cloud = WordCloud(background_color = "white", max_words = 500, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.png")

dataset = dataset.lower()
create_word_cloud(dataset)



"""
	dataset = open("data.csv", "r").read()

	def create_word_cloud(string):
	   maskArray = npy.array(Image.open("pngwave.png"))
	   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
	   cloud.generate(string)
	   cloud.to_file("wordCloud.png")

	dataset = dataset.lower()
	create_word_cloud(dataset)
"""
