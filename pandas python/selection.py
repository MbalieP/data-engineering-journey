import  pandas as pd

df = pd.read_csv("C:/Users/User/Documents/Data Engineering/personal_learn/pandas python/pokemon.csv")

#Selection  by column

print(df["Name"]) 
# print(df["Name"].to_string()] id f we want to print the whole database
print(df["Height"])
print(df["Height"].to_string)
print(df["Weight"])
print(df["Weight"].to_string)

#multiple COLUMN selections

print(df[["Name","Height","Weight"]])
print(df[["Name","Height","Weight"]].to_string())

#SELECT BY ROWS
df = pd.read_csv("C:/Users/User/Documents/Data Engineering/personal_learn/pandas python/pokemon.csv", index_col = "Name")
print(df.loc["Pikachu"])



