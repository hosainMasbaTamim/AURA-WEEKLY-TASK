# basic seaborn

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "x": ["a","b","c","d"],
    "y": [10, 20, 15, 30],
    "z": np.random.rand(4)
})

sns.barplot(data=df, x="x", y="y")
plt.show()

sns.lineplot(data=df, x="x", y="y")
plt.show()

sns.scatterplot(data=df, x="y", y="z")
plt.show()

h = np.random.rand(5,5)
sns.heatmap(h)
plt.show()

sns.pairplot(df)
plt.show()
