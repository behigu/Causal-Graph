import pandas as pd
from my_logger import logger

def read_csv(file_name):
  try:
    logger.info(f"{file_name} : Reading")
    null_values = ["n/a", "na", "undefined"]
    df = pd.read_csv(f'../data/{file_name}', na_values=null_values)
    logger.info("Reading Files Done!")
    return df
  except:
    logger.error(f"File Not Found : {file_name}")
