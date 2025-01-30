from functools import lru_cache
import pandas as pd

@lru_cache(maxsize=None)
def get_dataset():
    print("Loading data...") # Debug print to verify caching
    df = pd.read_csv("owid-co2-data.csv")
    df = df[df['year'] >= 1850]
    
    return df