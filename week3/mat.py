# basic matplot lib

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

print(x)
print(y)

plt.plot(x, y)
plt.title("line plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.scatter(x, y)
plt.title("scatter")
plt.show()

plt.bar(x, y)
plt.title("bar")
plt.show()

plt.hist(y)
plt.title("hist")
plt.show()

t = np.linspace(0, 2*np.pi, 100)
s = np.sin(t)

print(t)
print(s)

plt.plot(t, s)
plt.title("sine")
plt.show()
