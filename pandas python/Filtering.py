import pandas as pd
# Flitering = keeping the rows that match a condition


df = pd.read_csv("pokemon.csv")

tall_pokemon = df[df["height"] >= 2]
heavy_pokemon = df[df["Weight"] >= 100]
legendary_pokemon = df[df["Legendary"] == True ]
water_polemon = df[(df["Type 1"] == "water") |
                  (df["Type 2"] == "water") ]

fire_polemon = df[(df["Type 1"] == "Fire") &
                  (df["Type 2"] == "fly") ]
                    


print(tall_pokemon)
print(heavy_pokemon)
