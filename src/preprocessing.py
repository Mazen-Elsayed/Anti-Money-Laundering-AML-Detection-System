import os
import pandas as pd
import numpy as np


def drop_constant_and_high_missing(df, thresh=0.6):
	n = len(df)
	drop_cols = [c for c in df.columns if df[c].nunique(dropna=False) <= 1 or (df[c].isna().sum() / n) > thresh]
	return df.drop(columns=drop_cols), drop_cols


def combine_datetime(df, date_col='Date', time_col='Time', timestamp_col='timestamp'):
	if date_col in df.columns and time_col in df.columns:
		df[timestamp_col] = pd.to_datetime(df[date_col].astype(str) + ' ' + df[time_col].astype(str), errors='coerce')
	elif date_col in df.columns:
		df[timestamp_col] = pd.to_datetime(df[date_col], errors='coerce')
	return df


def fill_missing(df, num_strategy='median'):
	num_cols = df.select_dtypes(include=[np.number]).columns
	for c in num_cols:
		if df[c].isna().any():
			val = df[c].median() if num_strategy == 'median' else df[c].mean()
			df[c] = df[c].fillna(val)

	cat_cols = df.select_dtypes(include=['object', 'category']).columns
	for c in cat_cols:
		if df[c].isna().any():
			df[c] = df[c].fillna('unknown')

	return df


def encode_categoricals(df, max_unique_for_dummies=20):
	obj_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
	for col in obj_cols:
		nunique = df[col].nunique(dropna=False)
		if nunique <= max_unique_for_dummies:
			dummies = pd.get_dummies(df[col].astype(str), prefix=col)
			df = pd.concat([df.drop(columns=[col]), dummies], axis=1)
		else:
			df[col] = df[col].astype('category').cat.codes
	return df


def preprocess(df, drop_thresh=0.6, date_col='Date', time_col='Time', save_path=None):
	df2 = df.copy()
	df2, dropped = drop_constant_and_high_missing(df2, thresh=drop_thresh)
	df2 = combine_datetime(df2, date_col=date_col, time_col=time_col)
	df2 = fill_missing(df2)
	df2 = encode_categoricals(df2)

	if save_path:
		os.makedirs(os.path.dirname(save_path), exist_ok=True)
		df2.to_csv(save_path, index=False)

	return df2


def save_cleaned(df, output_path):
	os.makedirs(os.path.dirname(output_path), exist_ok=True)
	df.to_csv(output_path, index=False)
