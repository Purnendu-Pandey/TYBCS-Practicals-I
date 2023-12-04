import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame(columns=["Name","Age","Percentage"])
df.loc[0]=["Sankalp",21,94]
df.loc[1]=["Manas",20,94]
df.loc[2]=["Om",19,94]
df.loc[3]=["Raj",22,94]
df.loc[4]=["Rahul",19,74]
df.loc[5]=["Aman",20,84]
df.loc[6]=["Shwan",20,82]
df.loc[7]=["Gauraj",23,90]
df.loc[8]=["Sarthak",21,72]
df.loc[9]=["Satyam",21,88]
print(df)

print("Shape of data:",df.shape);
print("No of Rows and Columns:",df.size);
print("Data Types:",df.dtypes);
print("Feature Names:",df.info());
print("Description Of Data\n",df.describe());

df.loc[10]=["Purnendu",20,None]
df.loc[11]=["Shruti",20,82]
df.loc[12]=["Devesh",None,90]
df.loc[13]=["Shreyash",21,72]
df.loc[14]=["Shobhit",21,None]
df["remark"]=None
print(df)

print("Number of observation:",df.info());
print("Missing values:\n",df.isnull());
print("Duplicate values:\n",df.duplicated());

df.drop(columns="remark",axis=1,inplace=True)
print(df)

df.plot(x="Name",y="Percentage");
plt.title("Line Plot");
print(plt.show());

df.plot.scatter(x="Name",y="Percentage");
plt.title("Line Plot");
print(plt.show());

"""
output :-
ty32@pc38:~/TYBCS-32/FDS/Assignment No-1$ python3 setA1.py
      Name  Age  Percentage
0  Sankalp   21          94
1    Manas   20          94
2       Om   19          94
3      Raj   22          94
4    Rahul   19          74
5     Aman   20          84
6    Shwan   20          82
7   Gauraj   23          90
8  Sarthak   21          72
9   Satyam   21          88
Shape of data: (10, 3)
No of Rows and Columns: 30
Data Types: Name          object
Age            int64
Percentage     int64
dtype: object
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, 0 to 9
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Name        10 non-null     object
 1   Age         10 non-null     int64 
 2   Percentage  10 non-null     int64 
dtypes: int64(2), object(1)
memory usage: 320.0+ bytes
Feature Names: None
Description Of Data
              Age  Percentage
count  10.000000   10.000000
mean   20.600000   86.600000
std     1.264911    8.382521
min    19.000000   72.000000
25%    20.000000   82.500000
50%    20.500000   89.000000
75%    21.000000   94.000000
max    23.000000   94.000000
        Name   Age Percentage remark
0    Sankalp    21         94   None
1      Manas    20         94   None
2         Om    19         94   None
3        Raj    22         94   None
4      Rahul    19         74   None
5       Aman    20         84   None
6      Shwan    20         82   None
7     Gauraj    23         90   None
8    Sarthak    21         72   None
9     Satyam    21         88   None
10  Purnendu    20       None   None
11    Shruti    20         82   None
12  Devesh  None         90   None
13  Shreyash    21         72   None
14   Shobhit    21       None   None
<class 'pandas.core.frame.DataFrame'>
Index: 15 entries, 0 to 14
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Name        15 non-null     object
 1   Age         14 non-null     object
 2   Percentage  13 non-null     object
 3   remark      0 non-null      object
dtypes: object(4)
memory usage: 600.0+ bytes
Number of observation: None
Missing values:
      Name    Age  Percentage  remark
0   False  False       False    True
1   False  False       False    True
2   False  False       False    True
3   False  False       False    True
4   False  False       False    True
5   False  False       False    True
6   False  False       False    True
7   False  False       False    True
8   False  False       False    True
9   False  False       False    True
10  False  False        True    True
11  False  False       False    True
12  False   True       False    True
13  False  False       False    True
14  False  False        True    True
Duplicate values:
0     False
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9     False
10    False
11    False
12    False
13    False
14    False
dtype: bool
        Name   Age Percentage
0    Sankalp    21         94
1      Manas    20         94
2         Om    19         94
3        Raj    22         94
4      Rahul    19         74
5       Aman    20         84
6      Shwan    20         82
7     Gauraj    23         90
8    Sarthak    21         72
9     Satyam    21         88
10  Purnendu    20       None
11    Shagun    20         82
12  Devesh    None         90
13  Shreyash    21         72
14   Shobhit    21       None
None
"""

