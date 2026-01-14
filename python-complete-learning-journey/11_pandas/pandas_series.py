"""Pandas Series examples and practice."""

import pandas as pd


def series_example():
    s = pd.Series([1,3,5,7], index=['a','b','c','d'])
    return s


# Practice (5):
# 1) Filter series by condition.
# 2) Create series from dict with missing values.
# 3) Reindex and fill missing values.
# 4) Convert series to datetime index and resample.
# 5) Apply rolling windows to a series.

if __name__ == "__main__":
    print(series_example())
    s = pd.Series([1, None, 3])
    print('fill', s.fillna(0))
