import random

"""
Script de python que simula a un juego de adivinanzas 
el programa genera un numero aleatorio entre 1 y 15 y el usuario debe de adivinarlo en 3 intentos
"""

def juego():
    numero_a_adivinar = random.randint(1,15)
    intentos_maximos = 3
    intentos_realizados = 0

    print('Bienvenido al juego de adivinanzas!')
    print('Pensare en un numero y tu adivinaras cual es.')
    print('Tienes 3 intentos\n\n')

    while intentos_realizados < intentos_maximos:
        try: 
            adivinanza = int(input('Ingresa un numero: '))
        except Exception as e:
            print('El dato ingresado no es un numero, reintente')
            break

        if adivinanza == numero_a_adivinar:
            print('\nGANASTE, adivinaste el numero')
            print(f'El numero fue {numero_a_adivinar}')
            break
        else:
            print(f'Vuelve a intentar, el numero {adivinanza} no es el que pense')
            intentos_realizados += 1
        
        if intentos_realizados == intentos_maximos:
            print('\nTe quedaste sin intentos, vuelve a jugar')
            print(f'El numero que pense era: {numero_a_adivinar}')
    


def main():
    juego()

if __name__ == '__main__':
    main()