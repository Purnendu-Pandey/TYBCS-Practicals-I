from pandas import *
from numpy import *
from matplotlib.pyplot import *
df=read_csv("Iris.csv")
data=df['Species']
hist(data,edgecolor="k",linewidth=2,bins=3,alpha=0.8)
show()
