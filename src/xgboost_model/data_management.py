import pandas as pd
import joblib

from xgboost_model import config

def load_dataset(file_name):
    df = pd.read_csv(f"{config.DATASET_DIR}/{file_name}")
    return df


def save_model(model, version):
    save_file_name = f"{config.MODEL_NAME}{version}.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name
    joblib.dump(model, save_path)


def load_pipeline(file_name):
    """Load a persisted pipeline."""

    file_path = config.TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model