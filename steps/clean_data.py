import logging
import pandas as pd
from zenml import step

@step
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    import logging
import pandas as pd
from zenml import step

@step
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    # Log the input DataFrame shape
    logging.info(f"Input DataFrame shape: {df.shape}")
    
    # Example cleaning operations (you can customize based on your needs)
    
    # Drop any rows with missing values
    df_cleaned = df.dropna()
    
    # Log the cleaned DataFrame shape
    logging.info(f"Cleaned DataFrame shape: {df_cleaned.shape}")
    
    # Return the cleaned DataFrame
    return df_cleaned
