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

df2.dtypes    #Shows datatypes of all columns
# print(df2.dtypes)


df2.columns   #Displays all the columns in the dataframe 
print(df2.columns)

df2.index 
print(df2.index)    #Gives us the range of index values from start to end of data 

# One thing we must closely observe is that "index" and "columns" and "dtypes" are not functions, they are attributes 

print(df2)
print(df2.describe())   #Describe: Describe function gives us some statistical information about the numerical columns of the data 


print(df2.info())  #Info gives us range if index values and the datatypes of all columns 

#One thing to note is that we can see, only "Doors" and "Odometer" are shown as int64. Other columns datatypes is Object. 
#Hence all numeric operations are only happening on the integer columns from the data we have 