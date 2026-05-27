from collections import deque
from copy import deepcopy

l = [10,20,30,40,50]
print(l)
l.append(60)
print(l)
last_value = l.pop()
print(l)
print(last_value)

l.insert(0,-10)
print(l)
first_value = l.pop(0)
print(first_value)

d = deque(l)
print(d)

d.appendleft(-10)
print(d)


# immuable

a = 1 
b = 1
print(hex(id(a)))
print(hex(id(b)))
b = b*2
print(hex(id(a)))
print(hex(id(b)))
a=2

print(50*'-')

l = [10,20,30,40,50]

# l1 = l.copy()
l1 = l[:] # shallow copy
l[0] = 1000
print("l",l)
print("l1",l1)
l1[0] = 22
print("l",l)
print("l1",l1)

l2 =[
    [10,20,30], # 0
    [40,50,60], # 1
    [70,80,90], # 2
]
# l3 = l2[:]
l3 = deepcopy(l2)
# l2[1] = [1000,2000,3000]
# print(l2[1][1])
print("l2",l2)
print("l3",l3)
l2[1][1] = 500
print(l2)
print(l3)



a = [10,20,30,40]
print(a)
del a[1]
print(a)