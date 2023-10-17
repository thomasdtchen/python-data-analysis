import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
print(data)
data = data.cumsum()
print(data)
print("------------------------------------------------")
# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
print(data)
print("------------------------------------------------")
data = data.cumsum()
print(data)
# plot methods:
#'bar', 'hist', 'box', 'kde', 'area', 'scatter', 'hexbin', 'pie'
#data.plot()
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)
plt.show()
