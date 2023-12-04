from pandas import *
from numpy import *
from matplotlib.pyplot import * 
df=read_csv("Iris.csv")
data1=df['Species']
data2=df['Id']
bar(data1,data2)
show()
