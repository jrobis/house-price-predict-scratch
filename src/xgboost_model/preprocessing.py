from xgboost_model import config


def drop_nas(df):
    df = df.copy()
    df.dropna(subset=['price'], inplace=True)
    df[config.target] = df.price.str.replace(r'\D+', '').astype(int)
    return df


def rename_cols(df):
    df = df.copy()
    df.rename(columns=config.var_rename_dict, inplace=True)
    return df

def label_encoding(df):
    df = df.copy()

    df[config.categorical_vars] = df[config.categorical_vars].astype('category')
    for var in config.categorical_vars:
        df[var] = df[var].cat.codes

    return df