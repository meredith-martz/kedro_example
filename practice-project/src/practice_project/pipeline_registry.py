"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from practice_project.pipelines import data_processing as dp
from practice_project.pipelines import data_science as ds



def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_training_pipeline = ds.create_training_pipeline()
    data_science_inference_pipeline = ds.create_inference_pipeline()

    return {
        "__default__": data_processing_pipeline + data_science_training_pipeline,
        "data_processing": data_processing_pipeline,
        "training": data_processing_pipeline + data_science_training_pipeline,
        "inference": data_processing_pipeline + data_science_inference_pipeline
    }
