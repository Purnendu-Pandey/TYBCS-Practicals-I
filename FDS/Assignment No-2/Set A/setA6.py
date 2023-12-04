import numpy as np
import scipy.stats as s
import pandas as pd
d={"Name":["Ravi","Suraj","Meena","Rajesh","Sankalp"],"percentage":[80,70,90,89,92],"age":[19,20,21,22,21]}
df=pd.DataFrame(d)
print(df)
print("Average age of student :",s.tmean(df['age']).round(2))
print("Average age of student :",s.tmean(df['percentage']).round(2))
print(df.describe())

"""
ty32@pc38:~/TYBCS-32/FDS/Assignment No-2$ python3 setA6.py
      Name  percentage  age
0     Ravi          80   19
1    Suraj          70   20
2    Meena          90   21
3   Rajesh          89   22
4  Sankalp          92   21
Average age of student : 20.6
Average age of student : 84.2
       percentage        age
count    5.000000   5.000000
mean    84.200000  20.600000
std      9.176056   1.140175
min     70.000000  19.000000
25%     80.000000  20.000000
50%     89.000000  21.000000
75%     90.000000  21.000000
max     92.000000  22.000000
"""
