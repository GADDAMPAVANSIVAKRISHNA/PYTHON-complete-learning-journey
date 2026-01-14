"""Pandas DataFrame examples and practice."""

import pandas as pd


def dataframe_example():
    df = pd.DataFrame({'name':['A','B'],'score':[90,85]})
    return df


# Practice (5):
# 1) Groupby and aggregate operations.
# 2) Merge and join dataframes.
# 3) Pivot and unpivot data.
# 4) Handle missing values with different strategies.
# 5) Use apply/transform to create new columns.

if __name__ == "__main__":
    print(dataframe_example())
    df = pd.DataFrame({'name':['A','A','B'], 'score':[10,20,30]})
    print(df.groupby('name').mean())
