import random

def menu():
    print('Selecciona del menu una de las siguientes opciones: ')
    humano = ''
    try: 
        opcion=input('\n1. Papel\n2. Tijeras\n3. Piedra\n>>')
        opcion = int(opcion)
    except Exception as e:
        print(e)
    
    if opcion == 1:
        humano = 'Papel'
    elif opcion == 2:
        humano = 'Tijeras'
    elif opcion == 3:
        humano = 'Piedra'

    return humano


def computadora():
    computadora = random.randint(1,3)
    comp_opcion = ''
    if computadora == 1:
        comp_opcion = 'Papel'
    elif computadora == 2:
        comp_opcion = 'Tijeras'
    elif computadora == 3:
        comp_opcion = 'Piedra'
    
    return comp_opcion

def juego(humano, computadora):
    if humano == computadora:
        return 'Empate'
    elif (humano == "Piedra" and computadora == "Tijeras") or \
         (humano == "Papel" and computadora == "Piedra") or \
         (humano == "Tijeras" and computadora == "Papel"):
        return "Ganaste"
    else:
        return "Perdiste" 


def main():
    print('*' * 90)
    print('Bienvenido al juego de piedra papel y tijeras')
    while True:
        humano = menu()
        comp = computadora()
        print(f'Has elegido {humano}')
        print(f'\nYo elegi {comp}')

        resultado = juego(humano, comp)
        print(f'\nEl resultado es {resultado}')
        try:
            jugar = input('\nQuieres jugar de nuevo?: \n1. Si\n2. No\n>>')
            jugar = int(jugar)
        except Exception as e:
            print(e)

        if jugar != 1:
            break

if __name__ == '__main__':
    main()