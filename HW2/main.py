# Homework Exercise 2 (HW2): Spring 2025
# @Data Analyst: < Maulahna Robinson, 01177202 >

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

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

# Task Five: Using mask to fill in missing data
date_mask = (gold['Date'] >= "1985-01-01") & (gold['Date'] <= "1985-01-04")
gold['CNY'] = gold['CNY'].mask(date_mask & gold['CNY'].isna(), gold['USD'] * 2.82)
print("\nMissing Gold Rates:\n",gold['CNY'])

# Task 6: Slice year 2021 and output the lowest
gold_rate_2021 = gold[gold['Date'].dt.year == 2021]
gold_2021_summary = gold_rate_2021.groupby(gold_rate_2021['Date'].dt.month)['INR'].agg(['mean', 'max', 'min'])
print("\nInr By Month:\n",gold_2021_summary)

lowest_usd_month = gold.loc[gold['USD'].idxmin(), 'Date']
lowest_usd_value = gold['USD'].min()
print("\nUSD:",lowest_usd_month,lowest_usd_value)

lowest_eur_month = gold.loc[gold['EUR'].idxmin(), 'Date']
lowest_eur_value = gold['EUR'].min()
print("\nEUR:",lowest_eur_month,lowest_eur_value)

lowest_inr_month = gold.loc[gold['INR'].idxmin(), 'Date']
lowest_inr_value = gold['INR'].min()
print("\nINR:",lowest_inr_month,lowest_inr_value,"\n")

# Task 7: Remarks and Lambda Function
gold['Prev_GBP'] = gold['GBP'].shift(1)  
gold['Next_GBP'] = gold['GBP'].shift(-1) 

gold['Remarks'] = gold.apply(lambda row: 'gold rally' if row['GBP'] > row['Prev_GBP'] and row['GBP'] > row['Next_GBP'] 
                             else ('bearish gold market' if row['GBP'] < row['Prev_GBP'] and row['GBP'] < row['Next_GBP'] 
                                   else 'stable'), axis=1)

gold.drop(columns=['Prev_GBP', 'Next_GBP'], inplace=True)

print("\n",gold[['Date','USD','EUR','GBP','INR','AED','CNY', 'Remarks']].head(10))

# Task 8: Seaborn chart
# In 2011 there was a sharp drop in the gold rate. 
# This is because of the euro area crsis.
# It was a multi year debt and finanical crisis. It started with
# the collasp of iceland's banking system
# Source: https://www.investopedia.com/terms/e/european-sovereign-debt-crisis.asp#:~:text=The%20European%20sovereign%20debt%20crisis%20was%20a%20financial%20crisis%20sparked,breaking%20up%20the%20European%20Union.
gold['Year'] = gold['Date'].dt.year
yearly_gold_rate = gold.groupby('Year')[['USD', 'EUR', 'GBP', 'INR', 'AED', 'CNY']].mean().reset_index()

sb.lineplot(data=yearly_gold_rate, x='Year', y='EUR', marker='o', color='blue')

plt.title("Yearly Gold Rate in EUR")     
plt.xlabel("Year")                       
plt.ylabel("Gold Rate (EUR)")          

plt.xticks(yearly_gold_rate['Year'])     
plt.grid(True)                     
plt.show()