

class DivBy12Error(Exception):

    def __init__(self) -> None:
        super().__init__('Division par 12 !!!!! ohhhhhhh ⚠️ ')

def div(a:int,b:int)->float:
    """
    Division de a par b
     - a: le numérateur
     - b: le dénominateur
     - return: le résultat de la division
     - raise ZeroDivisionError: si b est égal à 0
     - raise DivBy12Error: si b est égal à 12
     - raise TypeError: si a ou b ne sont pas des entiers
     - raise ValueError: si a ou b sont des entiers négatifs
    """
    if b==12:
        # raise Exception('Division par 12 !!!!! ohhhhhhh ⚠️ ')
        raise DivBy12Error()
    return a/b

def call_div(a,b):
    r = 0

    
    print("OPEN log file")
    try:
        r = div(a,b)
    finally:
        print("CLOSE log file")
    
    return r

def main():

    try:
        a = 2
        # b = int(input('Valeur de b:'))
        b=12
        c = call_div(a,b)

        print(c)
    except ZeroDivisionError as e:
        print("Erreur",e)
    # except TypeError as e:
    #     print("Erreur",e)
    # except ValueError as e:
    #     print("Erreur",e)
    except DivBy12Error as e:
        print("Erreur DivBy12Error",e)
    except Exception as e:
        print("Erreur",e)
    else:
        print("s'éxécute s'il n'y a pas eu d'erreur")
    finally:
        print("la fin du code")

if __name__=='__main__':
    main()
