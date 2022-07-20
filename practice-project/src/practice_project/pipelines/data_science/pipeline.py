"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import split_data, train_model, apply_model, report_r_squared


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["mpg_clean", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
            ),
            node(
                func=apply_model,
                inputs=["regressor", "X_test"],
                outputs="y_test_pred",
                name="apply_model_node",
            ),
            node(
                func=report_r_squared,
                inputs=["y_test_pred", "y_test"],
                outputs=None,
                name="report_r_squared_node",
            ),
        ]
    )
