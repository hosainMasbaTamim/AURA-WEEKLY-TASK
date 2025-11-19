import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

add = a + b
sub = a - b
mul = a * b
dot = np.dot(a, b)

mat = np.array([[1,2],[3,4]])

reshape = a.reshape((3,1))
mean = np.mean(a)
std = np.std(a)

rand = np.random.rand(3,3)

print(add)
print(sub)
print(mul)
print(dot)
print(mat)
print(reshape)
print(mean)
print(std)
print(rand)

a = np.array([10, 20, 30, 40, 50])
first = a[0]
last = a[-1]
mid = a[1:4]
step = a[0:5:2]

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
row = m[1]
col = m[:,1]
block = m[0:2, 1:3]
rev = m[::-1]

print(first)
print(last)
print(mid)
print(step)
print(row)
print(col)
print(block)
print(rev)
