"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import drop_features, split_data, train_model, apply_model, report_r_squared, drop_inference_target


def create_training_pipeline(**kwargs) -> Pipeline:
    pipeline_instance = pipeline(
        [
            node(
                func=drop_features,
                inputs=["mpg_clean", "params:model_options"],
                outputs=["mpg_reduced_feature_set", "feature_set"],
                name="drop_features_node",
            ),
            node(
                func=split_data,
                inputs=["mpg_reduced_feature_set", "params:model_options"],
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
                name="training_apply_model_node",
            ),
            node(
                func=report_r_squared,
                inputs=["y_test_pred", "y_test"],
                outputs="metrics",
                name="training_report_r_squared_node",
            ),
        ]
    )
    ds_pipeline_1 = pipeline(
        pipe=pipeline_instance,
        inputs="mpg_clean",
        outputs="regressor",
        namespace="active_modelling_pipeline",
    )
    ds_pipeline_2 = pipeline(
        pipe=pipeline_instance,
        inputs="mpg_clean",
        namespace="candidate_modelling_pipeline",
    )
    return pipeline(
        pipe=ds_pipeline_1 + ds_pipeline_2,
        inputs="mpg_clean",
        namespace="data_science",
    )


def create_inference_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=drop_inference_target,
                inputs=["mpg_clean", "params:model_options"],
                outputs=["X_inference", "y_inference"],
                name="drop_inference_target_node",
            ),
            node(
                func=apply_model,
                inputs=["regressor", "X_inference"],
                outputs="y_inference_pred",
                name="inference_apply_model_node",
            ),
            node(
                func=report_r_squared,
                inputs=["y_inference_pred", "y_inference"],
                outputs=None,
                name="inference_report_r_squared_node",
            ),
        ],
        namespace="model_inference",
        inputs=["regressor", "mpg_clean"],
        outputs=None,
    )
