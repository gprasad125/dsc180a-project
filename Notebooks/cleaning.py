import pandas as pd
import numpy as np

def clean_state(state):
    if "{" in state:
        return state[1:-1]
    return state

def get_year(bday):
    
    if not pd.isnull(bday):
        
        return int(bday[0:4])