# Maulahna Robinson
# Activity Six
# CS620

import pandas as pd

url = "https://www.cs.odu.edu/~sampath/courses/data/values.csv"
data = pd.read_csv(url)

print("Imported Data:\n",data,"\n") # Make sure the data is loading in

column1 = (data['factor_1'])

column1_average = round(column1.mean(),2) 
print("The average of column 1 is", column1_average,"\n")

column1_std = round(column1.std(),2)
print("The standard deviation of column 1 is", column1_std,"\n")

selected_rows = data.iloc[[4,2,5]][['factor_1','price']]

print("Selected rows:\n",selected_rows)

