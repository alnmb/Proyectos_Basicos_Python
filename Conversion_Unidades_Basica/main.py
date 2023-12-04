import os
"""
Script que convierte temperaturas de celcius a fahrenhei
o de fahrenheit a celsius
"""
def c_to_f(celsius):
    """
    Funcion que retorna la conversion de temperatura C° a F°

    ARGS:
        celsius: temperatura a convertir
    """
    f = celsius * (9/5) + 32
    return (f)

def f_to_c(fah):
    """
    Funcion que retorna la conversion de temperatura F° a C°

    ARGS:
        fah: temperatura a convertir
    """
    c = (fah - 32) * (5/9)
    return (c)

def main():
    line = "*" * 50
    opcion = ""
    res = 0
    continuar = True
    while continuar:
        os.system('clear')
        print(line + '   MENU   ' + line)
        try:
            menu = input('\n\nSeleccione del menu\n1. C° a F°\n2. F° a C°\n\n>>')
            menu = int(menu)
        except Exception as err: 
            print(f'Ingrese solamente numeros, \nerror: {err}')
            break
        print(line)

        try:
            temp = int(input('\nIngrese la temperatura\n>>'))
        except Exception as err:
            print(f'Ingrese solamente numeros, error:\n{err}')
            break

        if menu == 1:
            opcion = 'Celsius a Fahrenheit'
            res = c_to_f(temp)
        elif menu == 2:
            opcion = 'Fahrenheit a Celisus'
            res = f_to_c(temp)

        print(f'El resultado de la conversion de {opcion} es: {res}')
        cont = input()
        if cont == 'salir':
            continuar = False
        



if __name__ == '__main__':
    main()