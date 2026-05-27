a = 2

if a==2:
    print("exactement a==2")
elif a==3:
    print("exactement a==3")
else:
    print(" ni l'un ni l'autre")

print( 50*'-')

l = ["Ligne 01","Ligne 02","Ligne 03"]


for v in l:
    print(v)


# for i in range(2,16,2):
for i in range(3):
    print(l[i])


# 0, Ligne 01
# 1, Ligne 02
# 2, Ligne 03
print( 50*'-')
for i in range(len(l)):
    print(str(i)+" "+l[i])
    print(i,l)

print( 50*'-')



is_found = False
for i in range(5):
    if i == 20:
        print(i,"ok")
        is_found = True
        # continue
        break
    print(i)
# else:
#     print("pas trouvé")


print("la fin")


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
r = http_error(400)
print(r)


def fib(n):    # write Fibonacci series less than n
    """
    Print a Fibonacci series less than n.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n=4):    # write Fibonacci series less than n
    """
    Return a Fibonacci series less than n.
    """
    a, b = 0, 1
    l=[]
    while a < n:
        l.append(a)
        a, b = b, a+b
    
    return l

# Now call the function we just defined:
fib(5)

l =[0,1]
l.append(2)
print(l) # [0,1,2]

r = fib2(5) # [0,1,1,2,3]
print(r)


r = fib2()
print(r)






# i = 5
# def f(v=i):
#     print(v)

# i = 1000
# f()


name="fred"
def hello():
    global name
    name = "fredo"
    print(name)


print(name) # fred
hello()
print(name) # fredo



def hello2():
    the_name = "fredo"
    print(the_name)

    a=4

hello2()

def hello3():
    # name
    if True:
        name = "fred"
    print(name)

print(50*'-')

def hello4(name,first_name):
    print(name,first_name)

hello4("GAURAT","Fred") #  positional arguments
hello4(first_name="Fred",name="GAURAT") # keywords arguments