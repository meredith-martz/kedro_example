"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""
import pandas as pd


def handle_na(x: pd.DataFrame) -> pd.DataFrame:
    return x.dropna()


def remove_name_of_car(x: pd.DataFrame) -> pd.DataFrame:
    return x.drop(columns=['name', 'origin'])



