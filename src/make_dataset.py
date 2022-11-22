# imports 
import pandas as pd
import numpy as np


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

############################################

def make_dataset():

    try:
        # read in file 
        filepath = "../data/raw/sampleData.csv"
        df = pd.DataFrame(filepath)

        # drop columns, NaN values
        df.drop(columns = ["userid_str", "status_id_str", "id"], inplace = True, errors = "ignore")
        df.dropna(inplace = True)

        # add or reshape columns using lambdas & UDFs 
        df["year"] = df["birth"].apply(lambda x: int(x[0:4]))
        df["term_partisanship"] = df["term_partisanship"].apply(clean_state)
        df["term_state"] = df["term_state"].apply(clean_state)
        df["posted"] = df["date"].apply(lambda x: int(x[0:4]))
        df["age_when_posted"] = df["posted"] - df["year"]

        # convert cleaned DataFrame to csv
        new_filepath = "../data/out/tweets_cleaned.csv"
        df.to_csv(new_filepath)
        
        return 'success'
    except:
        return 'fail'