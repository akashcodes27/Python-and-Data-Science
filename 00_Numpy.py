"""
We Gonna Learn Some pandas



In Pandas, for dealing with structured datasets,  We shall be working with 2 kinds of data structures: 
1. One-Dimensional Data Structure: Series  (Appears like a single column in output screen)
2. Two-Dimensional Data Structure: DataFrame (Appears like a table od rows and columns in output screen)


Difference between Series and DataFrames. Series takes Python's Lists as input. DataFrames take Python's Dictionaries as input
"""

import pandas as pd 

s1 = pd.Series(["BMW", "Honda", "Audi", "Mazda", "Lexus"])

s2 = pd.Series(["Red", "White", "Brown", "Grey", "Black"])

s3 = pd.Series(["2020", "2018", "2024", "2017", "2019"])


"While Constructing dataframes we can simply create individual Series and combine them inside DataFrame dictionary"

df1 = pd.DataFrame({ "Brand":s1, "Color":s2, "Year":s3})

# print(df1)


df2 = pd.read_csv("car-sales (1).csv")

# print(df2) 

print(df2.dtypes)
