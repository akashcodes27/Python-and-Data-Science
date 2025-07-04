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


print(df2.mean(numeric_only=True))  #We need to explicitely mention numeric_only=True 

print(df2.sum())   #Takes the sum, for string (or Object dtype) it simply concatenates 

s2 = pd.Series([200, 250, 190, 178, 340, 290])
print("Printing Series info")
print(s2.mean())
print(s2.sum())


#Lets say if instead of finding statistical information of the entire dataframe, if we only want statistical information of a specific column in the dataset, then we do the following:
print("Printing statistical information of specific columns of the dataframe instead of entire dataframe ")
print(df2["Odometer (KM)"].mean())
print(df2["Doors"].mean())
print(df2["Doors"].sum())
print(df2["Odometer (KM)"].mean())

print(len(df2))  #To retrieve the length of the dataframe (Basically total number of columns)

print(df2.head())   #Displays first 5 rows of the dataframe
print(df2.tail())   #Displays the last 5 rows of the dataframe 


print(df2)
print(df2.loc[5])   #loc basically gives us the row that is stored inside the specified index value 
print(df2.loc[2])
print(df2.loc[9])

print(df2.iloc[5])
print(df2.iloc[2])

print(df2.head(4))    #Both accomplish same results
print(df2.iloc[:4])

print(df2.iloc[2:7])  #Returns results by slicing to the specified range 

print(df2["Make"])


print(df2[df2["Make"] == "Toyota"])  #Similar to how we impose the WHERE clause in SQL 
print(df2[df2["Make"] == "Nissan"])
print(df2[df2["Odometer (KM)"] > 100000])


'''This is a Pandas operation, where:

✅ df2 is a pandas DataFrame.
✅ df2["Make"] selects the “Make” column from the DataFrame.
✅ df2["Make"] == "Toyota" creates a Boolean Series — it will be True wherever the “Make” column has the value "Toyota" and False elsewhere.
✅ df2[ <boolean series> ] uses Boolean indexing to filter only those rows where the condition is True. '''

# So basically if we have a df["columnName"] with us, and if we want to apply a filter to it to only retrieve entries from that specific column that satisfy a condition then we use the concept of Boolean Series and Boolean Indexing 
# df["Make"] == "Toyota" is a boolean series which implies a specific condition 
# df[ df["Make"] == "Toyota" ] is a boolean indexing method which applies the filter to the column 

print(df2)
print(pd.crosstab(df2["Price"], df2["Doors"]))


print(df2)

# Lets say we want to group by "Make" and want to find Odometer average reading for every make

print(df2.groupby("Make")["Odometer (KM)"].mean())
# In this case we have specified explicitely the column that we want to "GroupBy" and the Column that we wanna Aggregate


print(df2.groupby(["Make"]).mean(numeric_only=True))
# Here we mention the column that we wanna groupby but not the column that we wanna aggregate, so it aggregates all numeric columns

print(df2)

print(pd.crosstab(df2["Make"], df2["Doors"]))
# So what does crosstab do? Crosstab allows us to compare 2 columns on 2 axis (x and y), and the corresponding values in the table denote the frequency values. Eg: Against Colour=Red, Make="Honda", there will be a number like 2 which denotes that there exist 2 rows or cars with Make=Honda and Colour=Red 

print(df2)


# This is how we converted the string price into a numeric price
# We first got rid of the "$", then we got rid of  ","
# Then we converted to float, then we converted to int 
df2["Price"] = df2["Price"].str.replace("$", "", regex=False)
df2["Price"] = df2["Price"].str.replace(",", "", regex=False)
df2["Price"] = df2["Price"].astype(float).astype(int)

print(df2)

# str.replace() was one of the many data manipulation functions. There are more data manipulation functions out there. We shall take a look 

# Anything that you can do on strings in python, you can do all those operations on columns in pandas 

df2["Make"] = df2["Make"].str.lower()
print(df2)

df2["Colour"] = df2["Colour"].str.upper()

print(df2)


df3 = pd.read_csv("car-sales-missing-data.csv")

print(df3)

df3["Odometer"] = df3["Odometer"].fillna(df3["Odometer"].mean())

print(df3)

df3["Make"] = df3["Make"].str.upper()

print(df3)

# df3.dropna(inplace=True)
# print(df3)


# WAYS TO CREATE A COLUMN IN DATAFRAME


# ASSIGNING SERIES TO DATAFRAME COLUMN
# We can also assign Series to DataFrame column 
# lets say we have 

car_series = pd.Series([5,5,5,5,5,5])

df3["New Column"] = car_series 

print(df3)

df3["New Column"].fillna(4, inplace=True)

print(df3)



# ASSIGNING PYTHON LIST TO DATAFRAME COLUMN
# We can also assign a python list to DataFrame Column
# Make sure length of list is same as length of dataframe column, when assigning list to dataframe column
fuel_economy = pd.Series([9.5, 8.4, 7.6, 10, 12, 8.7, 4.7, 9, 10, 15])

df3["Fuel Economy per 100KM"] = fuel_economy   

print(df3)


# CREATING A DATAFRAME FROM A SINGLE VALUE
df3["Cylinders"] = 6

print(df3)


# Now lets see how we can change the order of the data. When we clean data to train machine learning models, we should change the order of the data sample to avoid any bias or overfitting. So we randomize the data 

# Now lets randomize the data we have 
# We can also specify other values in "frac", which allows us to control the amount of data we wish to randomize
print(df3)
# df3 = df3.sample(frac=1)
randomized_df = df3.sample(frac=1)
print(randomized_df)


print(df2)


# We can also apply mathematical operations to our dataframes by using apply+lambda 
# apply+lambda allows us to define our own function for the input provided in the form of: lambda x

df2["Price_after_tax"] = df2["Price"].apply(lambda x: x * 1.10)

print(df2)