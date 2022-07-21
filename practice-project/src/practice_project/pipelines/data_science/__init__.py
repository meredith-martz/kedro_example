"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.2
"""

from .pipeline import create_training_pipeline
from .pipeline import create_inference_pipeline


__all__ = ["create_pipeline"]

__version__ = "0.1"
