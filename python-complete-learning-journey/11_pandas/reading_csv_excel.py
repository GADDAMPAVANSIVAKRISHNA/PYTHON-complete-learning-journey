"""Reading CSV & Excel with pandas and practice."""

import pandas as pd


def read_csv(path):
    return pd.read_csv(path)


# Practice (5):
# 1) Read CSV and clean NA values.
# 2) Read Excel with multiple sheets and combine them.
# 3) Read CSV in chunks for large files and aggregate incremental results.
# 4) Parse dates on read and set as index.
# 5) Use dtype hints to optimize memory usage on large datasets.

if __name__ == "__main__":
    print('Use read_csv on your dataset')
