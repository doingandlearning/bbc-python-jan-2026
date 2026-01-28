import pandas as pd

df = pd.read_csv("movies.csv")

print(df.describe())
print(df.head())
print(df.tail())
print(df.sample(5))

df["Genre"] = df["Genre"].str.upper()
print(df.tail())