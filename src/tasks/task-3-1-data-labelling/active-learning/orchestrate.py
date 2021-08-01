import time
import os
import pandas as pd
import pickle
import sqlalchemy
from sklearn.model_selection import cross_val_score
import tensorflow as tf
from tensorflow import keras
from superintendent.distributed import ClassLabeller
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline


"""
WE NEED CSV WITH:
- title of content
- body of content (uncleaned) for human comprehension
- body of content (cleaned) for model
"""


# useful functions
def evaluate_model(model, x, y):
    score = cross_val_score(model, x, y, scoring = "accuracy", cv = 3)
    print(score)
    if not os.path.isdir("/app/models/"):
        os.mkdir("/app/models")
    save_time = time.asctime(time.time())
    filepath = "/app/models/{}".format(save_time)
    pickle.dump(model, open(filepath, "wb"))
    return score

def preprocessor(x, y):
    return x["title"] + " " + x["clean_selftext"], y

def wait_for_db(db_string):
    database_up = False
    connection = sqlalchemy.create_engine(db_string)
    while not database_up:
        time.sleep(2)
        try:
            print("attempting connection...")
            connection.connect()
            database_up = True
            print("connected!")
        except sqlalchemy.exc.OperationalError:
            continue


# create model
# baseline logistic regression model
model_baseline = Pipeline([
    # encode to utf8, decode, strip accent, lowercase, rm punct, rm stopwords (should I do this?), analyze by words, vectorize, tokenize
    ("tfidf_vectorizer", TfidfVectorizer(strip_accents = "unicode", lowercase = True, stop_words = "english")), # max_df = 0.95, min_df = 0.05
    ("logistic_regression", LogisticRegression(solver = 'lbfgs', multi_class = "multinomial", max_iter = 5000)) # prob output
])
# nn model
max_features = 10000
embedding_dim = 16
def modelling(): # change this model according to suitability for text data
    model = keras.models.Sequential([
        keras.layers.Embedding(max_features + 1, embedding_dim),
        keras.layers.Dropout(0.2),
        keras.layers.GlobalAveragePooling1D(),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(8, activation = "relu"),
        keras.layers.Dense(1)])
    model.compile(keras.optimizers.Adam(), keras.losses.CategoricalCrossentropy())
    return model
model_nn = Pipeline([
    ("tfidf_vectorizer", TfidfVectorizer(strip_accents = "unicode", lowercase = True, stop_words = "english")), 
    ("keras_classifier", keras.wrappers.scikit_learn.KerasClassifier(modelling, epochs = 5))
])
# use transfer learning!
# bert -- to try/ linear SVM -- try?


# link up with database
user = os.getenv("POSTGRES_USER")
pw = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_string = f"postgresql+psycopg2://{user}:{pw}@db:5432/{db_name}"
wait_for_db(db_string) # wait fo db to start up


# create widget
widget = ClassLabeller(
    connection_string = db_string,
    model = model_baseline,
    eval_method = evaluate_model,
    acquisition_function = "entropy", # experiment with this - take note of imabalanced data, output of model
    shuffle_prop = 0.1,
    model_preprocess = preprocessor, # model_preprocess = lambda x, y: (str(x["title"]) + " " + str(x["clean_selftext"]), y),
)


# add data where db is empty
if len(widget.queue) == 0:
    data = pd.read_csv("/app/clean_fulldata.csv")
    data = data[["title", "selftext", "clean_selftext"]]
    # there are some cases with NAN but not all columns NAN, so here we replace NAN with ""
    data.fillna(value = "", inplace = True)
    widget.add_features(data)
# retrain model every 30 sec and when we have 10 labels
if __name__ == "__main__": 
    widget.orchestrate(interval_seconds = 30, interval_n_labels = 10)