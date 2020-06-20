from xgboost_model import config
from xgboost_model.data_management import load_dataset, save_pipeline
from xgboost_model.preprocessing import DropNas
# from xgboost_model.features import create_type_var, create_additional_vars
# from xgboost_model import __version__ as _version

# import xgboost as xgb
# from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from xgboost_model import pipeline


def run_training():

    df = load_dataset(file_name=config.TRAINING_DATA_FILE)
    drop_nas = DropNas()
    df = drop_nas.transform(df)
    # df = create_type_var(df)
    # df = create_additional_vars(df)
    # df = rename_cols(df)
    # df = label_encoding(df)

    X_train, X_test, y_train, y_test = train_test_split(df
                                                    , df[config.target]
                                                    , test_size=config.test_size
                                                    , random_state=config.random_state)

    # xg_reg = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.3, learning_rate=0.1,
    #                           max_depth=5, alpha=10, n_estimators=10)

    # xg_reg.fit(X_train, y_train)

    pipeline.price_pipe.fit(X_train, y_train)

    save_pipeline(pipeline=pipeline.price_pipe)

    # return xg_reg


if __name__ == "__main__":
    model = run_training()
    # save_model(model, _version)
