import pandas as pd
df=pd.read_csv("data.csv");
print("Describing the data\n")
print(df.describe())
print("..............................................")
print("Shape of the dataset:",df.shape)
print("..............................................")
print("Display first 3 rows from dataset:\n",df.head(3))
print("..............................................")
print(df.isnull())
print("Missing values:",df.fillna(0,inplace=True))
print(df)
print("..............................................")
df.fillna(0)
print(df)
print("..............................................")
mean_age=df['Age'].mean()
print("Mean Of Age:",mean_age)
print("..............................................")
mean_salary=df['Salary'].mean()
print("Mean Of Salary:",mean_salary)
print("..............................................")
df['Age'].fillna(mean_age,inplace=True)
df['Salary'].fillna(mean_salary,inplace=True)
print(df)
"""
ty32@pc38:~/TYBCS-32/FDS/Assignment No-3$ python3 setA1.py
Describing the data :

             Age         Salary
count   8.000000       9.000000
mean   36.750000  119333.333333
std     8.084376  174157.974265
min    22.000000   48000.000000
25%    33.750000   54000.000000
50%    37.500000   61000.000000
75%    41.000000   72000.000000
max    48.000000  583000.000000
..............................................
Shape of the dataset: (10, 4)
..............................................
Display first 3 rows from dataset:
    Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  22.0  48000.0       Yes
2  Germany  30.0  54000.0        No
..............................................
   Country    Age  Salary  Purchased
0    False  False   False      False
1    False  False   False      False
2    False  False   False      False
3    False  False   False      False
4    False  False    True      False
5    False  False   False      False
6    False   True   False      False
7    False  False   False      False
8    False   True   False      False
9    False  False   False      False
Missing values: None
   Country   Age    Salary Purchased
0   France  44.0   72000.0        No
1    Spain  22.0   48000.0       Yes
2  Germany  30.0   54000.0        No
3    Spain  38.0   61000.0        No
4  Germany  40.0       0.0       Yes
5   France  35.0   58000.0        No
6    Spain   0.0   52000.0        No
7   France  48.0   79000.0       Yes
8  Germany   0.0  583000.0        No
9   France  37.0   67000.0       Yes
..............................................
   Country   Age    Salary Purchased
0   France  44.0   72000.0        No
1    Spain  22.0   48000.0       Yes
2  Germany  30.0   54000.0        No
3    Spain  38.0   61000.0        No
4  Germany  40.0       0.0       Yes
5   France  35.0   58000.0        No
6    Spain   0.0   52000.0        No
7   France  48.0   79000.0       Yes
8  Germany   0.0  583000.0        No
9   France  37.0   67000.0       Yes
..............................................
Mean Of Age: 29.4
..............................................
Mean Of Salary: 107400.0
..............................................
   Country   Age    Salary Purchased
0   France  44.0   72000.0        No
1    Spain  22.0   48000.0       Yes
2  Germany  30.0   54000.0        No
3    Spain  38.0   61000.0        No
4  Germany  40.0       0.0       Yes
5   France  35.0   58000.0        No
6    Spain   0.0   52000.0        No
7   France  48.0   79000.0       Yes
8  Germany   0.0  583000.0        No
9   France  37.0   67000.0       Yes
"""
