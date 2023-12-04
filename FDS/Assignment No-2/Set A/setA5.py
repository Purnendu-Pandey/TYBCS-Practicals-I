import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
nums=np.array([0.5,0.7,1,1.2,1.3,2.1])
bins=np.array([0,1,2,3])
print("nums  :",nums)
print("nums  :",bins)
print("\n")
plt.hist(nums,bins,edgecolor="orange",alpha=0.4)
plt.show()

"""
ty32@pc38:~/TYBCS-32/FDS/Assignment No-2$ python3 setA5.py
nums  : [0.5 0.7 1.  1.2 1.3 2.1]
nums  : [0 1 2 3]
"""
