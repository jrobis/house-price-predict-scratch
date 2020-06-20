import pathlib
#Look at the below line and PACKAGE_ROOT. Why isn't just "import xgboost_model" working

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
TRAINING_DATA_FILE = "properties-80210.csv"

MODEL_NAME = "xgboost"
PIPELINE_SAVE_FILE = f"{MODEL_NAME}_v"

target = "price"
random_state = 17
test_size = 0.3

var_rename_dict = {
    "real estate provider": "provider"
}

KEEP_FEATURES = ['postal_code', 'provider', 'type', 'bed_count', 'bath_count', 'sqft']

categorical_vars = ['provider', 'type', 'postal_code']

sample_data = {
    "postal_code": 0
    ,"price": 500000
    ,"provider": 12
    ,"type": 4
    ,"bed_count": 4.0
    ,"bath_count": 2.5
    ,"sqft": 3500.0
}



