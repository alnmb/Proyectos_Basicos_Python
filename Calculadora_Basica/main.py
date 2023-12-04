import os


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
    return a/b

def main():
    line = "*" * 50
    continuar = True
    while continuar:
        os.system('clear')
        print(line + '   MENU   ' + line)
        try:
            menu = input('\n\nSeleccione del menu\n1. Suma\n2. Resta\n3.Multiplicacion\n4.Division\n\n>>')
            menu = int(menu)
        except Exception as err: 
            print(f'Ingrese solamente numeros, \nerror: {err}')
            break
        print(line)

        try:
            a = int(input('\nIngrese el primer numero\n>>'))
            b = int(input('\nIngrese el segundo numero\n>>'))
        except Exception as err:
            print(f'Ingrese solamente numeros, error:\n{err}')
            break

        if menu == '1':
            opcion = 'suma'
            res = suma(a,b)
        elif menu == '2':
            opcion = 'resta'
            res = resta(a,b)
        elif menu == '3':
            opcion = 'multiplicacion'
            res = multiplicacion(a,b)
        elif menu == '4':
            opcion = 'division'
            res = division(a,b)

        print(f'El resultado de la operacion de {opcion} es: {res}')
        cont = input()
        if cont == 'salir':
            continuar = False
        

if __name__ == "__main__":
    main()

