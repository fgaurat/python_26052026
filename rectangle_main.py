from rectangle import Rectangle
from carre import Carre


def main():
    r = Rectangle(10, 5)
    print(r.longueur)
    # print(r.get_longueur())# 10

    r.longueur = 12
    print(r.longueur)

    # r.set_longueur(12)
    # print(r.get_longueur()) # 12

    # r.set_largeur(1)
    # print(r.get_largeur())
    print(r.surface())


    s = str(r)
    print(r)

    print(50*'-')
    c = Carre(2)
    print(c.surface())# 4 ?
    print(c)

if __name__=='__main__':
    main()
