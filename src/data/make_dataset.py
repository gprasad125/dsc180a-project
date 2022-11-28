# imports
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


############################################

# User Defined Cleaning Functions

def clean_state(state):
    if pd.isnull(state) == False:
        if "{" in state:
            state = state[1:-1]
    else:
        state = "Unknown"

    return state

def get_year(bday):

    if not pd.isnull(bday):

        return int(bday[0:4])

stop_words = set(stopwords.words('english'))

def text_cleaning(text):
    
    text = text.lower()
    text = re.sub('[^A-Za-z0-9\s]', '', text)
    tokens = [x for x in word_tokenize(text) if x not in stop_words]
    reshape_text = " ".join(tokens)
    return reshape_text

def handle_score(score):
    
    if pd.isnull(score):
        return score
    
    score = int(score)
        
    if score > 5.0:
        score = 5.0
    elif score < 1.0:
        score = 1.0
        
    return score

############################################

def make_dataset(inpath, outpath):

    # read in filepath RELATIVE to run.py
    df = pd.read_csv(inpath)

    # add or reshape columns using lambdas & UDFs
    df["year"] = df["birth"].apply(lambda x: int(x[0:4]))
    df["term_partisanship"] = df["term_partisanship"].apply(clean_state)
    df["term_state"] = df["term_state"].apply(clean_state)
    df["posted"] = df["date"].apply(lambda x: int(x[0:4]))
    df["age_when_posted"] = df["posted"] - df["year"]
    df['text'] = df['text'].apply(text_cleaning)
    df['relevant'] = df['Bucket'].apply(lambda bkt: bkt == "1")
    df['score'] = df['SentimentScore'].apply(handle_score)

    # drop unneeded columns
    df.drop(
        columns = [
            "userid_str", "status_id_str", "id", "Bucket", "SentimentScore", 
        ],
        inplace = True,
        errors = 'ignore'
    )

    # convert cleaned DataFrame to csv
    df.to_csv(outpath, index = False)
