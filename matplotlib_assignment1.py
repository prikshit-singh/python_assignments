import matplotlib.pyplot as plt
  
plt.plot([1, 2, 3, 4], [1, 4, 9, 16],color="green",marker="o",linestyle="dashed",linewidth=2)
plt.axis([0, 6, 0, 20])

plt.title("lecture 1 assignment")
plt.xlabel("x-axis",color="green",fontsize=24)
plt.ylabel("y-axis")
plt.show()