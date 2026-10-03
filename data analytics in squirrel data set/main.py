
import pandas as pd


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv").reset_index()

df = data["Primary Fur Color"].value_counts()

df.columns = ["fur color","count"]

df.to_csv("Squirrel Fur Color.csv",index=True)
print(df)


