import pandas as pd
import numpy as np

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