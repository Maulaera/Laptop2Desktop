#  Maulahna Robinson
# CS 620
# Activity 8

import numpy as np
import pandas as pd 
import math 

array = np.random.randint(1,100,(3,5))
array_df = pd.DataFrame(array,index=['a','b','c'],columns=[1,2,3,4,5])
print("Generated Dataframe:\n",array_df)

df_sqrt = array_df.map(lambda x: math.sqrt(x))
print("\nSquare Root of Dataframe:",df_sqrt)

sum = df_sqrt.sum(axis=1)
print("\nSum of Rows:",sum)