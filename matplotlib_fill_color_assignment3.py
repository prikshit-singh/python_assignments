import numpy as np
from matplotlib import pyplot as plt
x= np.array(['jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec'])
y=np.array([100,200,300,400,500,600,700,800,900,1000,1100,1200])
x2=np.array(['jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec'])
y2= y*2
plt.plot(x,y,color="green",marker="o",linestyle="dashed",linewidth=2)
plt.plot(x2,y2,color="red",marker="*",linestyle="dashed",linewidth=1)
plt.title("lecture 2 assignment")
plt.xlabel("months",color="green")
plt.ylabel("in thousands",color="red")
plt.fill_between(x,y, y2,color='blue')
plt.ylim(0)
plt.legend(["Birth","Death"]);
 
# Show plot with grid
plt.grid()
plt.show()