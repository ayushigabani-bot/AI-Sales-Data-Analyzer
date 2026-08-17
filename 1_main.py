import pandas as pd 
import numpy as np 

df=pd.read_csv("data/sales_data.csv")
print("DATASET IMPORTED SUCCESFULLY")

print(df.head(10))

print(f"The Total Rows and Columns is := {df.shape}")

print(f"The Name of Columns is := {df.columns}")

print(f"The Datatype of Columns := {df.dtypes}")

print(df.isnull())

print(df.describe())   