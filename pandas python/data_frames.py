import pandas as pd

data = {"Name": ["spongebob","patrick","squidward"],
        "Age":[30,35,50]
}
#df = pd.DataFrame(data)
df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])


print(df)
print(df.loc["Employee 2"]) # selection by label
print(df.iloc[0]) # selectiob by iterger / index

# add a new column
df["job"] = ["cook","N/A","Cashier"]

print(df)

# add a new row
new_row = pd.DataFrame([{"Name": "Sandy","Age": 28,"job":"Engineer"}],
                       index=["Employee 4"])

df = pd.concat([df, new_row])

#add new rows
new_row = pd.DataFrame([{"Name": "Sandy","Age": 28,"job":"Engineer"},
                        {"Name": "Mr Crabs","Age": 60,"job":"manager"},
                        {"Name": "Mrs drive","Age": 8,"job":"driving instructor"}
                        ],
                       index=["Employee 4","Employee 5","Employee 6"])

df = pd.concat([df, new_row])



print(df)