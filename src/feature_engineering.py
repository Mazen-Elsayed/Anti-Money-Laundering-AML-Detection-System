import os
import pandas as pd
import numpy as np


def _find_col(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None


def add_log_amount(df, amount_col_candidates=('amount','Amount','AMOUNT')):
    col = _find_col(df, amount_col_candidates)
    if col is None:
        return df
    df['log_amount'] = np.log1p(df[col].astype(float).fillna(0))
    return df


def extract_datetime_features(df, timestamp_col_candidates=('timestamp','Timestamp','date','datetime')):
    col = _find_col(df, timestamp_col_candidates)
    if col is None:
        return df
    ts = pd.to_datetime(df[col], errors='coerce')
    df['hour'] = ts.dt.hour
    df['weekday'] = ts.dt.weekday
    return df


def account_aggregates(df,
                       sender_candidates=('nameOrig','NameOrig','sender','Sender_account','Sender'),
                       receiver_candidates=('nameDest','NameDest','receiver','Receiver_account','Receiver'),
                       amount_candidates=('amount','Amount')):
    sender_col = _find_col(df, sender_candidates)
    receiver_col = _find_col(df, receiver_candidates)
    amount_col = _find_col(df, amount_candidates)

    df_out = df.copy()
    # If required columns are missing, return original
    if sender_col is None and receiver_col is None:
        return df_out

    if amount_col is None:
        # fallback: create a zero amount column to avoid crashes
        df_out['_fe_amount'] = 0.0
        amount_col = '_fe_amount'

    # outgoing aggregates per sender
    if sender_col is not None:
        out_agg = df_out.groupby(sender_col)[amount_col].agg(['sum','count']).rename(columns={'sum':'total_outgoing','count':'num_outgoing'})
        df_out = df_out.merge(out_agg, left_on=sender_col, right_index=True, how='left')
    else:
        df_out['total_outgoing'] = 0.0
        df_out['num_outgoing'] = 0

    # incoming aggregates per receiver
    if receiver_col is not None:
        in_agg = df_out.groupby(receiver_col)[amount_col].agg(['sum','count']).rename(columns={'sum':'total_incoming','count':'num_incoming'})
        df_out = df_out.merge(in_agg, left_on=receiver_col, right_index=True, how='left')
    else:
        df_out['total_incoming'] = 0.0
        df_out['num_incoming'] = 0

    # number_transactions: sum of incoming and outgoing counts (may double-count same txn but useful)
    df_out['number_transactions'] = df_out[['num_outgoing','num_incoming']].sum(axis=1)

    # ensure numeric types
    for c in ['total_outgoing','total_incoming','num_outgoing','num_incoming','number_transactions']:
        if c in df_out.columns:
            df_out[c] = pd.to_numeric(df_out[c], errors='coerce').fillna(0)

    # drop helper col if created
    if '_fe_amount' in df_out.columns:
        df_out = df_out.drop(columns=['_fe_amount'])

    return df_out


def apply_feature_engineering(df, save_path=None):
    df2 = df.copy()
    df2 = add_log_amount(df2)
    df2 = extract_datetime_features(df2)
    df2 = account_aggregates(df2)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        df2.to_csv(save_path, index=False)

    return df2


def save_features(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
# Placeholder for feature engineering functions
