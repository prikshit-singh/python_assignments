import pandas as pd
import matplotlib.pyplot as plt


dataFrame = pd.DataFrame([["A",100],["B", 0, 200],["C",0,400],["D",150,0],["E",0,400]
])


dataFrame.plot.bar(stacked=True, title='Car Specifications', color=("orange", "cyan"))
plt.xticks(rotation=90)
plt.show()