# Homework Exercise 2 (HW2): Spring 2025
# @Data Analyst: < Maulahna Robinson, 01177202 >

import pandas as pd

# Task One: Load data file into Pandas Data frame called "Gold"
gold = pd.read_csv("daily_gold_rate.csv")

# Task Two: List Data Types of df_gold and the first 10 rows/items
print("Data Types:\n " , gold.dtypes)
print("\nGold Data Frame:\n", gold.iloc[0:10])

# Task Three: Conver to datetime format and list rows 100-150
gold['Date'] = pd.to_datetime(gold['Date'])
print("\nRows 100-150:\n" , gold.iloc[100:151])