# Maulahna Robinson
# Activity 10
# Feburary 13th, 2025

import pandas as pd

height = [159, 171, 158, 162, 162, 177, 160, 175, 168, 171, 178, 178, 173, 177, 164]
height.sort()  
print("Sorted Height List:", height)

data = {'h': height}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

def systematic_sampling(df, step):
    return df.iloc[::step]  # Select every 'step' row

sampled_df = systematic_sampling(df, 3)
print("\nSystematic Sample (Every 3rd Student):\n", sampled_df)
