# Maulahna Robinson
# Activity 11
# Feburary 13th, 2025

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://www.cs.odu.edu/~sampath/courses/data/brfss.csv"
df = pd.read_csv(url)

df = df.drop(columns=['sex'], errors='ignore')

df_scaled = (df - df.min()) / (df.max() - df.min())

print("Scaled DataFrame:\n", df_scaled.head())

plt.figure(figsize=(12, 6))
df_scaled.boxplot()
plt.title("Boxplot of Min-Max Scaled BRFSS Data")
plt.xticks(rotation=90)  
plt.show()
