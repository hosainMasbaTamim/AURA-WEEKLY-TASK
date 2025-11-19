# basic pandas

import pandas as pd
import numpy as np

# basic dataframe
data = {
    "name": ["alice", "bob", "carol", "dave"],
    "age": [25, 30, 22, 35],
    "salary": [50000, 60000, 45000, 70000]
}
df = pd.DataFrame(data)
print(df)

# head and tail
print(df.head(2))
print(df.tail(2))

# describe
print(df.describe())

# select column
print(df["name"])
print(df["age"])

# filter rows
print(df[df["age"] > 25])

# add new column
df["bonus"] = df["salary"] * 0.1
print(df)

# drop column
df_drop = df.drop("bonus", axis=1)
print(df_drop)

# sort values
print(df.sort_values("age"))

# group by
grouped = df.groupby("age")["salary"].sum()
print(grouped)

# basic operations
print(df["salary"] + 1000)
print(df["age"] * 2)

# sample random rows
print(df.sample(2))
