import numpy as np

array = np.array([[1,2,3], [2,3,4]])
print(array)
print("dim", array.ndim)
print("shape", array.shape)
print("size", array.size)


a = np.array([2,3,4], dtype=float)
print(a.dtype)

a = np.zeros( (3,4) )
print(a)
a = np.arange(10, 20, 2)
print(a)
a = np.arange(12).reshape((3,4))
print(a)
a = np.linspace(1, 10, 5)
print("linspace", a)

print("-------------------------           calculate          ----------------------------")
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a)
print(b)
c = a - b
print(c)
c = b**2
print(c)
print(b)
print(b<3)

d = np.array([90, 180])
print(np.sin(d))

a = np.array([[1,1],
              [0,1]])

b=np.arange(4).reshape((2,2))
print(a)
print(b)
print("------ c ------")
c = a*b
print(c)
print("------ c_dot ------")
c_dot = np.dot(a,b)
print(c_dot)
a = np.random.random((2,4))
print(a)
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print("------ statistic ------")
#axis=1 sum all column, y
print(np.sum(a, axis=1))
#axis=0 min all row, x
print(np.min(a, axis=0))
#把所有列拿出来整
print(np.max(a, axis=1))

print("-------------------------------statistic----------------------------------------")
A = np.arange(2, 14).reshape((3,4))
print(A)
print("argmin", np.argmin(A))
print("argmax", np.argmax(A))
print("mean", np.mean(A))
print("average", np.average(A))
print("median", np.median(A))
print("cumsum", np.cumsum(A))
print(np.diff(A))
print()
B = np.arange(14, 2, -1).reshape((3,4))
print(B)
print(np.sort(B))
print("----------------------------------transpose-------------------------------------")
print(A)
#print(np.transpose(A))
print(A.T)
print((A.T).dot(A))
print()
print(A)
print("np.clip(A,5,9)")
print(np.clip(A,5,9))
print()
print(A)

print(np.mean(A, axis=1))
print(np.mean(A, axis=0))
