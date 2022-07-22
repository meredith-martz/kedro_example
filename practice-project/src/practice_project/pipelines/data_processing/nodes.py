"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def handle_na(x: pd.DataFrame) -> pd.DataFrame:
    return x.dropna()


def handle_categorical(x: pd.DataFrame):
    enc = OneHotEncoder()
    enc_results = enc.fit_transform(x[['origin']])
    x = x.drop(columns=['name', 'origin'])
    col_names = np.concatenate(enc.categories_, axis=0)
    x = x.join(pd.DataFrame(enc_results.toarray(), columns=col_names))
    print(x.columns.tolist())
    return x

    #return x.drop(columns=['name', 'origin'])



