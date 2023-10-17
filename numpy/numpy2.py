# axis=0为行操作， axis=1为列操作
import numpy as np


a = np.zeros((2,2), dtype=int)
print(a)

# 替换某列
a[::,0] = [1, 1]
print(a)
print("-------------   -1 表示倒数第一   ----------------")
a[::,-1] = a[::,-1] + 3
print(a)

# 删除某列
b = np.delete(a,0,axis=1)
print(b)


print("---------- insert ---------")
print(a)
print(b)
c = np.insert(a, 0, values=b, axis=1)
print(c)
print("------------")
print(b)
a = np.zeros(len(b))
print(a)
b = np.insert(b, 0, values=a, axis=1)
print(b)