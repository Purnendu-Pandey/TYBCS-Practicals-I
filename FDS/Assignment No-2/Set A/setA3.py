import pandas as pd
from scipy.stats import iqr
import numpy as np
d={"score":[80,92,78,83,88],"Name":["Ravi","Suraj","Meena","Rajesh","Sankalp"]}
df=pd.DataFrame(d)
print(df)
r=max(df["score"])-min(df["score"])
print("Value of range in distribution:",r)
col=df["score"] 
mean_of_score=col.mean()
print("Average of score:",mean_of_score)
q3,q1=np.percentile(col,[72,25])
iqrvalue=q3-q1
print("Interquartile range :",iqrvalue)

"""
ty32@pc38:~/TYBCS-32/FDS/Assignment No-2$ python3 setA3.py
   score     Name
0     80     Ravi
1     92    Suraj
2     78    Meena
3     83   Rajesh
4     88  Sankalp

Value of range in distribution: 14
Average of score: 84.2
Interquartile range : 7.400000000000006
"""
