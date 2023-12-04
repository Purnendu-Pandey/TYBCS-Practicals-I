from numpy import*
from pandas import*
from matplotlib.pyplot import*
from seaborn as sns
df=read_csv("Iris.csv")
sns.boxplot(x=df["Species"],y=df["SepalLengthCm"],palette="Blues")
show()
