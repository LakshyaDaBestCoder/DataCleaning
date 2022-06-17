import pandas as pd
import csv

df=pd.read_csv("final.csv")

del df["Luminosity"]
del df["id"]
df = df.rename({
    "Star_name":"name",
    "Distance":"distance",
    "Mass":"mass",
    "Radius":"radius"
}, axis='columns')

df.to_csv('starMain.csv', index=False)