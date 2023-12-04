import pandas as pd
import numpy as np
import scipy.stats as s
df=pd.read_csv("Iris.csv")
print(df.sample(10))
print(df)
print(df.dtypes)

print("min and max value petalLengthCm :",max(df["SepalLengthCm"]))
print("min and max value petalLengthCm :",min(df["SepalLengthCm"]))

print("min and max value petalLengthCm :",max(df["PetalLengthCm"]))
print("min and max value petalLengthCm :",min(df["PetalLengthCm"]))
print(df.info())


print("mean")
print("SpealLengthCm mean : ",s.tmean(df["SepalLengthCm"]).round(2))
print("SpealWidthCm mean : ",s.tmean(df["SepalWidthCm"]).round(2))
print("PetalLengthCm mean : ",s.tmean(df["PetalLengthCm"]).round(2))
print("PetalWidthCm mean : ",s.tmean(df["PetalWidthCm"]).round(2))

print("median")
print("SpealLengthCm median : ",np.median(df["SepalLengthCm"]).round(2))
print("SpealWidthCm median: ",np.median(df["SepalWidthCm"]).round(2))
print("PetalLengthCm median: ",np.median(df["PetalLengthCm"]).round(2))
print("PetalWidthCm median : ",np.median(df["PetalWidthCm"]).round(2))

"""
output :-
ty32@pc38:~/TYBCS-32/FDS/Assignment No-2$ python3 setB1.py
      Id  SepalLengthCm  ...  PetalWidthCm          Species
101  102            5.8  ...           1.9   Iris-virginica
98    99            5.1  ...           1.1  Iris-versicolor
18    19            5.7  ...           0.3      Iris-setosa
147  148            6.5  ...           2.0   Iris-virginica
72    73            6.3  ...           1.5  Iris-versicolor
60    61            5.0  ...           1.0  Iris-versicolor
141  142            6.9  ...           2.3   Iris-virginica
5      6            5.4  ...           0.4      Iris-setosa
65    66            6.7  ...           1.4  Iris-versicolor
16    17            5.4  ...           0.4      Iris-setosa

[10 rows x 6 columns]
      Id  SepalLengthCm  ...  PetalWidthCm         Species
0      1            5.1  ...           0.2     Iris-setosa
1      2            4.9  ...           0.2     Iris-setosa
2      3            4.7  ...           0.2     Iris-setosa
3      4            4.6  ...           0.2     Iris-setosa
4      5            5.0  ...           0.2     Iris-setosa
..   ...            ...  ...           ...             ...
145  146            6.7  ...           2.3  Iris-virginica
146  147            6.3  ...           1.9  Iris-virginica
147  148            6.5  ...           2.0  Iris-virginica
148  149            6.2  ...           2.3  Iris-virginica
149  150            5.9  ...           1.8  Iris-virginica

[150 rows x 6 columns]
Id                 int64
SepalLengthCm    float64
SepalWidthCm     float64
PetalLengthCm    float64
PetalWidthCm     float64
Species           object
dtype: object
min and max value petalLengthCm : 7.9
min and max value petalLengthCm : 4.3
min and max value petalLengthCm : 6.9
min and max value petalLengthCm : 1.0
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             150 non-null    int64  
 1   SepalLengthCm  150 non-null    float64
 2   SepalWidthCm   150 non-null    float64
 3   PetalLengthCm  150 non-null    float64
 4   PetalWidthCm   150 non-null    float64
 5   Species        150 non-null    object 
dtypes: float64(4), int64(1), object(1)
memory usage: 7.2+ KB
None
mean
SpealLengthCm mean :  5.84
SpealWidthCm mean :  3.05
PetalLengthCm mean :  3.76
PetalWidthCm mean :  1.2
median
SpealLengthCm median :  5.8
SpealWidthCm median:  3.0
PetalLengthCm median:  4.35
PetalWidthCm median :  1.3
"""
