import matplotlib.pyplot as plt
import numpy as np
import math

np.random.seed(10)
data1 = np.random.normal(100,20,200)
data2 = np.random.normal(200,20,400)
data3 = np.random.normal(600,20,300)
data4 = np.random.normal(700,200,400)

data = [data1,data2,data3,data4]

fig = plt.figure(figsize = (10,7))
ax = fig.add_axes([0,0,1,1])
bp = ax.boxplot(data)
plt.show()