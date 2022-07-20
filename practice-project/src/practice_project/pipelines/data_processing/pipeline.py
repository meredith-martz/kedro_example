"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import remove_name_of_car

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=remove_name_of_car,
                inputs="mpg",
                outputs="mpg_clean",
                name="remove_name_of_car_node"
            ),
        ]
    )



