import numpy as np
import matplotlib.pyplot as plt
x=np.random.rand(50)
arr1=np.append(x,[2,3])
plt.boxplot(arr1)
plt.show()
