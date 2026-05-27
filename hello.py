# TheWorldIsFlat => PascalCase, UpperCamelCase
# theWorldIsFlat => camelCase
# the_world_is_flat => snake_case
# the-world-is-flat => kebab-case, spinal-case

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")
    print("Be careful not to fall off!")


s =  "L'orage gronde"
print(s)
s =  'L\'orage gronde'
print(s)

p="c:\\test\\new_project"
p=r"c:\test\new_project"
print(p)

m="""
ligne 01
ligne 02
ligne 03
""" 
print(m)

a = 1
b = "valeur de a:"+str(a)
b1 = f"valeur de a:{a}"
print(b)
a = 5
b = "toto"*a
print(b)

print(20*'-')
print("bonjour")
print(20*'-')

s = "Python" # 6 chars
print(s[0])
print(len(s))
print(s[len(s)-1])
print(s[-1])
print(s[2:4]) # [2:4[ th
print(s[2:5]) # [2:5[ thon
print(s[2:-1]) # [2:-1[ thon

s = "Python" # 6 chars
print(s[0:3]) # Pyt
print(s[3:-1]) # hon
print(s[:3]) # Pyt
print(s[3:]) # hon
print(s[:]) # Python
print(s[546:])