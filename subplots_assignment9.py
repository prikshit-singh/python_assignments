import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0,math.pi*2,0.05)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.tanh(x)

figure,axis = plt.subplots(2,2)
axis[0,0].plot(x,y1)
axis[0,1].plot(x,y2)
axis[1,0].plot(x,y3)
axis[1,1].plot(x,y4)
# plt.plot(x, y1)
plt.show()