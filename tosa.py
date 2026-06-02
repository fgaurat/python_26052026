l = [10, 20, 30, 40, 50]

print(l[1:3])
print(l[3:5])
print(l[3:])

l = [1, 2, 3]
     
# l.append(4,5))
l.extend([4,5])
print(l)

d = {"a": 1, "b": 2}
print(d.get("c",123556))


print(list(range(2, 10, 2)))

print( 50*'-')


class Truc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __enter__(self):
        print("enter with")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit with")
        return False    
    


print('avant le with')
with Truc(1,2) as t:
    print(t.a, t.b)
print('apres le with')