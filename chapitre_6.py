import fibo as fb
from fibo import fib
import sys
# masque la fonction fib du module fibo
# def fib(t):
#     print("local fib",t)

def f():
    pass


def main():
    print(sys.argv)
    fib_value = int(sys.argv[1])
    a = 12
    fb.fib(fib_value)
    fib(fib_value)
    f()


if __name__=='__main__':
    main()


    