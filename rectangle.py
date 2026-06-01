


class Rectangle:

    def __init__(self,a,b):
        self.__longueur = a
        self.__largeur = b

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self,l):
        if l >=0:
            self.__longueur = l        

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self,l):
        if l >=0:
            self.__largeur = l        

    def surface(self):
        return self.__longueur * self.__largeur

    def __str__(self):
        return f"{__class__.__name__} {self.__longueur=},{self.__largeur=}"


    longueur = property(get_longueur,set_longueur,doc="longueur getter")
    largeur = property(get_largeur,set_largeur,doc="largeur getter")
