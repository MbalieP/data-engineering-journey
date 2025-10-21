import pandas as pd

#reduces a set of values into a single value used to summarize 
# analyze data often used  with the grouby function

df = pd.read_csv("data.csv")

#whole dataframe
print(df.mean(numeric_only = True))
print(df.sum(numeric_only = True))
print(df.min(numeric_only = True))
print(df.max(numeric_only = True))
print(df.count())

#single column
print(df["Height"].mean())
print(df["Weight"].sum())
print(df["Height"].min())
print(df["Weight"].max())
print(df["height"].count())

#GROUP BY
group = df.groupby("type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].count())