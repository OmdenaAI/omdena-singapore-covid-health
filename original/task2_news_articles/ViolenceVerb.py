import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

from afinn import Afinn
afinn = Afinn()

def get_verb(doc):
    verbs = []
    try: 
        for token in doc:
            if token.pos_ == 'VERB':
                verbs.append(token.lemma_)  
        return verbs
    except:
        return ''      
        

def negative_verbs(verb):
    if afinn.score(verb) <0:
        return verb


#1k English articles
df_en = pd.read_csv('english_5k_label_final.csv')
df_en = df_en[df_en['lab_final']!= 'Irrelevant']
# df_en = df_en.dropna(subset=['lab_final'])
df_en['summary'] = df_en['summary'].apply(lambda x: x.lower())
df_en['doc'] = df['summary_wrap'].apply(nlp)
df_en['verbs'] = df_en['doc'].apply(lambda x: get_verb(x))
df_en['negative_verbs'] = df_en['verbs'].apply(lambda x: [i for i in x if afinn.score(i)<0])



#non english articles
df_nonen = pd.read_excel('non_english_labelled_new.xlsx')
df_nonen = df_nonen[df_nonen['label']!= 'Irrelevant']
df_nonen = df_nonen.dropna(subset=['label'])
df_nonen['summary_wrap'] = df_nonen['summary_wrap'].apply(lambda x: x.lower())
df_nonen['doc'] = df_nonen['summary_wrap'].apply(nlp)
df_nonen['verbs'] = df_nonen['doc'].apply(lambda x: get_verb(x))
df_nonen['negative_verbs'] = df_nonen['verbs'].apply(lambda x: [i for i in x if afinn.score(i)<0])


en_verbs=sum([i for i in df_en['negative_verbs']],[])
nonen_verbs=sum([i for i in df_nonen['negative_verbs']],[])
verbs = en_verbs + nonen_verbs

s = set(verbs)
len(s)
