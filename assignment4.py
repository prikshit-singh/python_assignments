import pandas as pd
import matplotlib.pyplot as plt


dataFrame = pd.DataFrame([["A",10, 20, 30, 40, 50, 60],["B", 12, 18, 15, 25, 22, 30],["C",70, 15, 50, 80, 90, 60]
])


dataFrame.plot.barh(stacked=True, title='Car Specifications', color=("orange", "cyan"))

plt.show()