import copy
from googletrans import Translator
from langdetect import detect
import pandas as pd

df = pd.read_csv('NONen_interim_01_05_ALL_IN.csv', index_col=False)

for index, row in df.iterrows():
    title = row['title']
    translator = Translator()
    try:
        lang = detect(title)
        if lang == 'en':
            df['translated'] = title
        else:
            df['translated'] = translator.translate(title, dest='en').text
    except Exception as e:
        print(str(e))
        continue
                
df.to_csv('NONen_interim_01_05_ALL_IN_with_full_titles_translated.csv')
