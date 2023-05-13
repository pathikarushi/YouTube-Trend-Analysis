import pandas as pd

df = pd.DataFrame({
    'id0': [1.71, 1.72, 1.72, 1.23, 1.71],
    'id1': [6.99, 6.78, 6.01, 8.78, 6.43],
    'id2': [3.11, 3.11, 4.99, 0.11, 2.88]})


def count_values_in_range(series, range_min, range_max):

    # "between" returns a boolean Series equivalent to left <= series <= right.
    # NA values will be treated as False.
    return series.between(left=range_min, right=range_max).sum()

    # Alternative approach:
    # return ((range_min <= series) & (series <= range_max)).sum()


range_min, range_max = 1.72, 6.43

df["n_values_in_range"] = df.apply(
    func=lambda row: count_values_in_range(row, range_min, range_max), axis=1)

print(df)