class A:
    
    def show(self):
        print("A")

class B(A):
    
    def show(self):
        print("B")

class C(A):
    
    def show(self):
        print("C")

class D(B,C):
    
    def show(self):
        print("D")
        super().show() #    B 
        super(B,self).show() # C
        super(C,self).show() # C


def main():
    d = D()
    d.show()

    print(D.mro())

if __name__=='__main__':
    main()
