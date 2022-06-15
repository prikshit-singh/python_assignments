import numpy as np
from matplotlib import pyplot as plt
x= np.array([1,2,3,4])
y=x*2
plt.plot(x,y,color="green",marker="o",linestyle="dashed",linewidth=2)
plt.title("lecture 2 assignment")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()