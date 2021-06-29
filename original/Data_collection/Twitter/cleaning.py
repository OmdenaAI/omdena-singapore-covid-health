# Text preprocessing functions

# !pip install nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn

STOPWORDS =  stopwords.words('english') + ['twitter','com']
punct = list(string.punctuation)
punct += ['’', '…']

def remove_URL(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+|pic\.twitter\S+')
    return url_pattern.sub(r'', text)

def remove_punctuations(text):
    for punctuation in punct:
        text = text.replace(punctuation, ' ')
    return text

def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

def remove_digits(text):
    return re.sub(r"\d", "", text)

def lemmatize_text(text):
    return " ".join([wn.morphy(word) if wn.morphy(word) != None 
                     else word 
                     for word in text.split()])

# Function to preprocess text in the passed column of the dataframe by combining ALL the above functions

def clean_text(df, col):
    print("Cleaning text and adding column 'processed_text'")
    df['processed_text'] = df[col]
    # Converting to lower case
    df['processed_text'] = df['processed_text'].str.lower()
    # Removing /n characters
    df['processed_text'] = df['processed_text'].apply(lambda x: x.replace('\n', ' '))
    # Removing urls
    df['processed_text'] = df['processed_text'].apply(lambda text: remove_URL(text))
    # Removing punctuations
    df['processed_text'] = df['processed_text'].apply(lambda text: remove_punctuations(text))
    # Removing the stopwords
    df['processed_text'] = df['processed_text'].apply(lambda text: remove_stopwords(text))
    # Remove the digits
    df[col]= df[col].apply(lambda text: remove_digits(text))
    # Lemmatization of text
    df['processed_text'] = df['processed_text'].apply(lambda text: lemmatize_text(text))
    print('DONE! \n')
