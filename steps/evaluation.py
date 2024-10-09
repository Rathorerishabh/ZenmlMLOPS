import logging
import pandas as pd
from zenml import step

@step
def evaluate_model(df: pd.DataFrame) -> None:
    """
    Evalaute the model on the ingested dataset"""
    pass