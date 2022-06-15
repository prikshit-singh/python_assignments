import matplotlib.pyplot as plt
import numpy as np
import math

np.random.seed(10)
data = np.random.normal(100,20,200)
fig = plt.figure(figsize = (10,7))
plt.boxplot(data)
plt.show()