# Python  26/05

SE26-205145

Frédéric Gaurat

https://www.m2iformation.fr/

https://github.com/fgaurat/python_26052026


https://docs.python.org/3/tutorial/interpreter.html
https://docs.python.org/3/tutorial/introduction.html


l = ["Ligne 01","Ligne 02","Ligne 03"]


https://docs.python.org/3.14/tutorial/controlflow.html#match-statements


https://docs.python.org/3.14/tutorial/controlflow.html#defining-functions

https://docs.python.org/3/library/functions.html

https://refactoring.guru/fr

https://docs.python.org/3.14/tutorial/datastructures.html


l = [10,20,30,40,50]

https://fr.wikipedia.org/wiki/Comparaison_asymptotique


https://wiki.python.org/moin/TimeComplexity.html


https://realpython.com/

https://www.mockaroo.com/



---

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


---



t = 1,2,3,4

print(t)
print(t[0])


a,b,*c,d = 0,1,2,3

print(a)
print(b)
print(c)
print(d)

s = 0,
print(s)

print(50*'-')

s = {"valeur 01","valeur 02","valeur 03","valeur 04","valeur 04","valeur 02"}
s1 = {"valeur 01","valeur 02"}

print(s)
print(s1)
print("diff",s-s1)

lines = ["ligne 01","ligne 01","ligne 02","ligne 03"]
print(lines)
lines = sorted(list(set(lines)))
print(lines)






---

	"Python main function": {
		"prefix": "pymain",
		"body": [
			"def main():",
			"\tpass$1",
			"",
			"if __name__=='__main__':",
			"\tmain()",
			"",
		],
		"description": "Python main function"
	}


---

result = "a={value_a} b={value_b} c={value_c}".format(value_a=a,value_b=b,value_c=c)
    print(result)

    d = {
        "value_a":a,
        "value_b":b,
        "value_c":c
    }





