import pandas as pd

# series = a pandas 1-dimensional labeled array that can hold any data type
#         think of it like a single column in a spreadsheet(1 dimensional)

data = [100,102,104]

series = pd.Series(data)

print(series)

data2 = [100.1,102.3,104.4]

series2 = pd.Series(data2)

print(series2)

letters = ["A","B","b"]

let_series = pd.Series(letters)

print(let_series)


bool = [True,False,True]

bool_series = pd.Series(bool)

print(bool_series)



data = [100,102,104]

series = pd.Series(data,index=["a","b","c"])

print(series)

series.loc["c"] = 200

print(series.loc["c"])
print(series.iloc[2])

example 4

data = [100,102,104,200,202]

series = pd.Series(data,index=["a","b","c","d","e"])

print(series)


print(series[series >= 200])

# series 5

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)
series.loc["Day 2"] += 500

print(series)
print(series.loc["Day 3"])

print(series[series < 2000])
print(series.iloc[2])