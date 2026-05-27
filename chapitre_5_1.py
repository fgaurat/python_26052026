

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


print(50*'-')

d = {
    "name":"Gaurat",
    "firstName":"Fred",
    "age":49,
    "jobs":['dev',"formation"]
}

print(d['firstName'])
print(d['name'])
print(d['jobs'][1])

keys = d.keys()
values = d.values()
print(keys)
print(values)
items =list(d.items())
print(items[0])
# a,b = 0,1
key,value = items[0]
print(key,value)
# for k in d:
#     print(k,d[k])
print("========")
for k,v in d.items():
    print(k,v)


lines = ["ligne 01","ligne 01","ligne 02","ligne 03"]


for i,line in enumerate(lines):
    print(i,line)