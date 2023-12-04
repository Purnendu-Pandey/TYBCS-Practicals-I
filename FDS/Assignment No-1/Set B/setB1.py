import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("SOCR-HeightWeight.csv");
df.head(10);
df.tail(10);
df.sample(20);
print(df);

print("Shape of dataframe:",df.shape);
print("Size of dataframe:",df.size);
print("Data Types:",df.dtypes);
print("Statistical Data:\n",df.describe());
print("Number of observation:",df.info());
print("missing values\n",df.isnull());
df["BMI"]=(df["Weight(Pounds)"]/(df["Height(Inches)"]**2));
print(df);

print("Maximum BMI :",df.BMI.max());
print("Minimum BMI :",df.BMI.min());

df.plot.scatter(x="Height(Inches)",y="Weight(Pounds)");
plt.title("Scatter Diagram");
print(plt.show());

"""
OUTPUT :-
ty32@pc38:~/TYBCS-32/FDS/Assignment No-1$ python3 setB1.py

       Index  Height(Inches)  Weight(Pounds)
0          1        65.78331        112.9925
1          2        71.51521        136.4873
2          3        69.39874        153.0269
3          4        68.21660        142.3354
4          5        67.78781        144.2971
...      ...             ...             ...
24995  24996        69.50215        118.0312
24996  24997        64.54826        120.1932
24997  24998        64.69855        118.2655
24998  24999        67.52918        132.2682
24999  25000        68.87761        124.8742

[25000 rows x 3 columns]
Shape of dataframe: (25000, 3)
Size of dataframe: 75000
Data Types: Index               int64
Height(Inches)    float64
Weight(Pounds)    float64
dtype: object
Statistical Data:
               Index  Height(Inches)  Weight(Pounds)
count  25000.000000    25000.000000    25000.000000
mean   12500.500000       67.993114      127.079421
std     7217.022701        1.901679       11.660898
min        1.000000       60.278360       78.014760
25%     6250.750000       66.704397      119.308675
50%    12500.500000       67.995700      127.157750
75%    18750.250000       69.272958      134.892850
max    25000.000000       75.152800      170.924000
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25000 entries, 0 to 24999
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Index           25000 non-null  int64  
 1   Height(Inches)  25000 non-null  float64
 2   Weight(Pounds)  25000 non-null  float64
dtypes: float64(2), int64(1)
memory usage: 586.1 KB
Number of observation: None
missing values
        Index  Height(Inches)  Weight(Pounds)
0      False           False           False
1      False           False           False
2      False           False           False
3      False           False           False
4      False           False           False
...      ...             ...             ...
24995  False           False           False
24996  False           False           False
24997  False           False           False
24998  False           False           False
24999  False           False           False

[25000 rows x 3 columns]
       Index  Height(Inches)  Weight(Pounds)       BMI
0          1        65.78331        112.9925  0.026111
1          2        71.51521        136.4873  0.026687
2          3        69.39874        153.0269  0.031773
3          4        68.21660        142.3354  0.030587
4          5        67.78781        144.2971  0.031402
...      ...             ...             ...       ...
24995  24996        69.50215        118.0312  0.024434
24996  24997        64.54826        120.1932  0.028848
24997  24998        64.69855        118.2655  0.028253
24998  24999        67.52918        132.2682  0.029005
24999  25000        68.87761        124.8742  0.026322

[25000 rows x 4 columns]
Maximum BMI : 0.03701443692089851
Minimum BMI : 0.018591137267932455
None

"""
