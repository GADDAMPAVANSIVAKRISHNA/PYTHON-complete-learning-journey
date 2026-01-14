"""Data cleaning examples with pandas."""

import pandas as pd


def drop_duplicates(df):
    return df.drop_duplicates()


# Practice (5):
# 1) Fill missing values with different strategies.
# 2) Detect outliers using IQR.
# 3) Normalize columns and scale numeric data.
# 4) Parse and standardize date columns.
# 5) Deduplicate using a subset of columns.

if __name__ == "__main__":
    print('Data cleaning examples')
