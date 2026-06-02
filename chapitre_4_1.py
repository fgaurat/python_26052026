
def add(*the_list):
    print(the_list)
    the_value = 0
    for v in the_list:
        # the_value = v+the_value
        the_value+= v
    
    return the_value

l = [10,20,30]
l1 = [40,50]
print(l) # [10,20,30]
print(*l) # 10,20,30


r = add(*l,*l1) #150 (10,20,30,40,50)
print("l,l1",r)
r = add(10,20,30,40,50) #150

print(r)

a = 12,12,45

print("valeur de a",12)


def hello(**kwargs):
    print(kwargs['name'])

hello(name="Gaurat",firstname="fred",age=49)



def hello2(a,b,/): # positional only
# def hello2(*,a,b): # keywords only
    print(a,b)


# hello2(a="toto",b="titi")
# hello2("toto","titi")

print(50*'-')

def mult2(the_list:list) -> list:
    """
    Multiplication par 2 des items
    """
    l2 = []
    for v in the_list:
        l2.append(v*2)

    return l2    


l = [10,20,30,40,50]

l2 = mult2(l) # [20,40,60,80,100]

def mult2_item(i):
    return i*2

# l2 = map(mult2_item,l)
# l2 = map(lambda i:i*2,l)
lamb = lambda i:i*2
l2 = map(lamb,l)


l2 = list(l2)
print(l2)



l2 = []
for i in l:
    l2.append(i*2)


a = 2
l2 = list(map(lambda i:i*2,l))

l2 = [i*2 for i in l] # comprehension list , liste par intention



def f(**kwargs):
    print(kwargs) # { 'a': 1, 'b': 2, 'c': 3 }
    # {name: "Gaurat", firstname: "fred", age: 49}

f(a=1,b=2,c=3)
f(name="Gaurat",firstname="fred",age=49)


print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))