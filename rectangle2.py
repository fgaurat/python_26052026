


class Rectangle2:

    def __init__(self,a,b):
        self.__longueur = a
        self.__largeur = b

    @property
    def longueur(self):
        return self.__longueur
    
    @longueur.setter
    def longueur(self,l):
        if l >=0:
            self.__longueur = l        
    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self,l):
        if l >=0:
            self.__largeur = l        

