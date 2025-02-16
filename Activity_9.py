# Maulahna Robinson 
# Activity 9
# Feburary 15th, 2025

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the URL
url = "https://www.cs.odu.edu/~sampath/courses/data/brfss.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print("Original DataFrame:\n", df.head())

# Function to clean the BRFSS dataset
def cleanBRFSSFrame(dataframe):
   
    dataframe = dataframe.drop(columns=['sex'], errors='ignore')


    dataframe = dataframe.dropna()

    return dataframe

cleaned_df = cleanBRFSSFrame(df)

# Display summary statistics for the 'weight2' column
print("\nSummary Statistics for 'weight2':\n", cleaned_df['weight2'].describe())

# Calculate and display the 25th, 50th, and 70th percentiles of 'age'
percentiles = [0.25, 0.50, 0.70]
age_percentiles = cleaned_df['age'].quantile(percentiles)
print("\nAge Percentiles:\n", age_percentiles)

# Create a Violin plot for 'height'
plt.figure(figsize=(8, 5))
sns.violinplot(data=cleaned_df['htm3'])
plt.title('Violin Plot of Height')
plt.xlabel('Height (htm3)')
plt.show()
