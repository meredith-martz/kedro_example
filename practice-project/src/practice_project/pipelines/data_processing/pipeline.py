"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import remove_categorical, handle_na

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=remove_categorical,
                inputs="mpg",
                outputs="mpg_wout_cat_col",
                name="remove_categorical_node"
            ),
            node(
                func=handle_na,
                inputs="mpg_wout_cat_col",
                outputs="mpg_clean",
                name="handle_na_node"
            ),
        ]
    )



