

def verificacion(numero):
    
    try:
        numero = int(numero)
    except Exception as e:
        print('El dato ingresado no es un numero, reintente')

    if numero %2 == 0:
        return 'par'
    else:
        return 'impar'
    


def main():
    print('Programa que verifica si un numero es par o impar\n')
    numero = input('Ingrese un numero: ')

    resultado = verificacion(numero)
    print(f'El numero {numero} es {resultado}')

if __name__ == '__main__':
    main()