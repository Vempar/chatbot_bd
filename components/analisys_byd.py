import pandas as pd
from database_byd import get_data

def load_byd_data():
    query = "SELECT * FROM database_byd"
    df = get_data(query)
    return df

print (load_byd_data)