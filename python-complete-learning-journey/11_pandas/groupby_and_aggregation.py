"""Groupby and aggregation examples."""

import pandas as pd


def group_mean(df, col):
    return df.groupby(col).mean()


# Practice (5):
# 1) Pivot tables and multiple aggregations.
# 2) Use transform vs agg.
# 3) Groupby with rolling and time-based grouping.
# 4) Filter groups using filter function.
# 5) Use custom aggregation functions for complex metrics.

if __name__ == "__main__":
    print('Groupby examples')
