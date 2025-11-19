# testing dependencies on system
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


arr = np.random.randint(1, 100, size=10)
print("NumPy Array:", arr)
print("Mean:", np.mean(arr))
print("Std Dev:", np.std(arr))


data = {
    "name": ["A", "B", "C", "D"],
    "score": [85, 90, 78, 92],
    "age": [20, 22, 19, 21]
}

df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nDescribe:")
print(df.describe())


plt.figure(figsize=(6, 4))
sns.barplot(x=df["name"], y=df["score"])
plt.title("Sample Bar Plot - Scores by Name")
plt.xlabel("Name")
plt.ylabel("Score")
plt.tight_layout()

plt.show()  
