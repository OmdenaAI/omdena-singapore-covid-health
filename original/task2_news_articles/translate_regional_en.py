import numpy as np
from googletrans import Translator
import pandas as pd
import copy
import subprocess

data= pd.read_csv('NONen_interim_01_05_ALL_IN_with_full_texts.csv') 
data.head()

def translate_text(text, dest_language="en"):
        # Used to translate using the googletrans library
        import json
        translator = Translator()
        try:
            translation = translator.translate(text=text, dest=dest_language)
        except json.decoder.JSONDecodeError:
            # api call restriction
            process = subprocess.Popen(["nordvpn", "d"], stdout=subprocess.PIPE)
            process.wait()
            process = subprocess.Popen(["nordvpn", "c", "canada"], stdout=subprocess.PIPE)
            process.wait()
            return translate_text(text=text, dest_language=dest_language)
        return translation

for index, row in data.iterrows():
    try:
    	translated = translate_text(row['texts'], dest_language='en')
        data['translated'] = translated.text
    except Exception as e:
    	print(str(e))
        continue
