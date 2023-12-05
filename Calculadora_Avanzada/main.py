import os
import math


def suma(a,b):
    """
    Funcion que retorna la suma de dos numeros

    ARGS:
        a: primer numero
        b: segundo numero
    """
    return (a + b)

def resta(a,b):
    """
    Funcion que retorna la resta de dos numeros

    ARGS:
        a: primer numero
        b: segundo numero
    """
    return (a - b)

def multiplicacion(a,b):
    """
    Funcion que retorna la multiplicacion de dos numeros

    ARGS:
        a: primer numero
        b: segundo numero
    """
    return a * b

def division(a,b):
    """
    Funcion que retorna la division de dos numeros

    ARGS:
        a: primer numero
        b: segundo numero
    """
    if b != 0:
        return a/b
    else:
        return "Error, no se puede dividir entre 0"

def potencia(a,b):
    """
    Funcion que retorna el primer numero a la potencia del segundo

    ARGS:
        a: numero base
        b: exponente
    """
    return a ** b
def raiz_cuadrada(a):
    """
    Funcion que retorna la raiz cuadrada del numero dado
    ARGS:
        a: numero a extraer raiz cuadrada
    """
    return math.sqrt(a)
def logaritmo(a, base):
    """
    Funcion que retorna el logaritmo
    ARGS:
        a: numero
        b: base
    """
    return math.log(a,base)

def main():
    line = "*" * 50
    continuar = True
    while continuar:
        os.system('clear')
        print(line + '   MENU   ' + line)
        try:
            menu = input("""\n\nSeleccione del menu\n1. Suma\n2. Resta\n3.Multiplicacion\n4.Division\n5.Potencia\n6.Raiz cuadrada\n7.Logaritmo\n>>""")
            menu = int(menu)
        except Exception as err: 
            print(f'Ingrese solamente numeros, \nerror: {err}')
            break
        print(line)

        try:
            if menu in (1,2,3,4,5,7):
                a = int(input('\nIngrese el primer numero\n>>'))
                b = int(input('\nIngrese el segundo numero\n>>'))
            if menu == 6:
                a = int(input('\nIngrese el primer numero\n>>'))
        except Exception as err:
            print(f'Ingrese solamente numeros, error:\n{err}')
            break

        if menu == 1:
            opcion = 'suma'
            res = suma(a,b)
        elif menu == 2:
            opcion = 'resta'
            res = resta(a,b)
        elif menu == 3:
            opcion = 'multiplicacion'
            res = multiplicacion(a,b)
        elif menu == 4:
            opcion = 'division'
            res = division(a,b)
        elif menu == 5:
            opcion = 'potencia'
            res = potencia(a,b)
        elif menu == 6:
            opcion = 'raiz cuadrada'
            res = raiz_cuadrada(a)
        elif menu == 7:
            opcion = 'logaritmo'
            res = logaritmo(a,b)

        print(f'El resultado de la operacion de {opcion} es: {res}')
        cont = input()
        if cont == 'salir':
            continuar = False
        

if __name__ == "__main__":
    main()

