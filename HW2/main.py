# Homework Exercise 2 (HW2): Spring 2025
# @Data Analyst: < Maulahna Robinson, 01177202 >

import pandas as pd
import numpy as np

# Task One: Load data file into Pandas Data frame called "Gold"
gold = pd.read_csv("daily_gold_rate.csv")

# Task Two: List Data Types of df_gold and the first 10 rows/items
print("Data Types:\n " , gold.dtypes)
print("\nGold Data Frame:\n", gold.iloc[0:10])

# Task Three: Conver to datetime format and list rows 100-150
gold['Date'] = pd.to_datetime(gold['Date'])
print("\nRows 100-150:\n" , gold.iloc[100:151])

# Task Four: USD NumPy Array
gold_filtered = gold[(gold['Date'].dt.year == 2020) |
                     (gold['Date'].dt.year ==2021)]

gold_usd_2020and2021 = gold_filtered['USD'].to_numpy()
# print("\nUSD Values: \n",gold_usd_2020and2021)
print("\nThe Median Gold Rate:\n", np.median(gold_usd_2020and2021))

print("\nUSD Gold Descending:\n", np.sort(gold_usd_2020and2021)[::-1])

range_price = np.max(gold_usd_2020and2021) - np.min(gold_usd_2020and2021)
range_price = round(range_price,2)
print("\nThe USD Range:\n",range_price)
