"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.2
"""
import logging
import pandas as pd
from typing import Tuple, Dict, Any

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data.drop(columns=parameters["target_column"])
    y = data[parameters["target_column"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"])

    return X_train, X_test, y_train, y_test

def drop_inference_target(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """

    :param data: Data containing features and target.
    :param parameters: Parameters defined in parameters/data_science.yml.
    :return: The data split into X and y where X is the features and y is the target.
    """

    X = data.drop(columns=parameters["target_column"])
    y = data[parameters["target_column"]]

    return X, y


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestRegressor:
    """Trains the random forest regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    regressor = RandomForestRegressor()
    regressor.fit(X_train, y_train)
    return regressor


def apply_model(
        regressor: RandomForestRegressor, X_test: pd.DataFrame
) -> pd.Series:
    """Calculates predictions.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
    """
    y_pred = regressor.predict(X_test)
    y_pred = pd.Series(y_pred)

    return y_pred


def report_r_squared(y_pred: pd.Series, y_true: pd.Series):
    """Calculates and logs the r^2.

    Args:
        y_pred: Predicted target.
        y_true: True target.
    """

    y_pred = y_pred.reset_index(drop=True)
    y_true = y_true.reset_index(drop=True)

    r2 = r2_score(y_true, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has r-squared of %.3f on provided data.", r2)

