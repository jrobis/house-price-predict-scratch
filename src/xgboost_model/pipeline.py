from sklearn.pipeline import Pipeline
import xgboost as xgb

from xgboost_model import preprocessing as pp
from xgboost_model import features
from xgboost_model import config

# df = load_dataset(file_name=config.TRAINING_DATA_FILE)
#     df = drop_nas(df)
#     df = create_type_var(df)
#     df = create_additional_vars(df)
#     df = rename_cols(df)
#     df = label_encoding(df)

price_pipe = Pipeline(
    [
        # (
        #     "drop_nas", pp.DropNas(),
        # ),
        (
            "create_type_var", features.CreateTypeVar(),
        ),
        (
            "create_additional_vars", features.CreateAdditionalVars(),
        ),
        (
            "rename_cols", pp.RenameCols(),
        ),
        (
            "label_encoding", pp.LabelEncoding(),
        ),
        (
            "keep_features", pp.KeepFeatures(),
        ),
        (
            "xgboost_model", xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.3, learning_rate=0.1,
                                              max_depth=5, alpha=10, n_estimators=10)
        ),
    ]
)