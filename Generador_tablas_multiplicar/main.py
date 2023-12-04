
def multiplicar(a,b):
    """Funcion que hace la tabla de multiplicar del numero dado
    Args: 
        a numero a multiplicar
        b numero de veces a multiplicar
    """
    try:
        numero_a_multiplicar = int(a)
        numero_de_repeticiones = int(b) + 1
    except Exception as e:
        print('los datos ingresados no son numeros, repita por favor')

    for x in range(1,numero_de_repeticiones):
        res = x * numero_a_multiplicar
        print(f'{numero_a_multiplicar} X {x} = {res}')




def main():
    print('Bienvenido a su generador de tablas de multiplicar\n')
    numero_a_multiplicar = input('De que numero quiere hacer su tabla de multiplicar: ')
    numero_de_repeticiones = input('Hasta que numero se debe multiplicar: ')
    print('\n')
    multiplicar(numero_a_multiplicar, numero_de_repeticiones)

if __name__ == '__main__':
    main()