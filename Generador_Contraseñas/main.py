import pyperclip
import random
import string

def gen_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(caracteres)for i in range(longitud))
    return result

def gen_contrasena_no_num(longitud):
    caracteres = string.ascii_letters + string.punctuation
    result = ''.join(random.choice(caracteres)for i in range(longitud))
    return result

def gen_contrasena_no_esp(longitud):
    caracteres = string.ascii_letters + string.digits
    result = ''.join(random.choice(caracteres)for i in range(longitud))
    return result

def imprimir(contrasena):
    print(f'La contraseña generada es: {contrasena}')
    print('La contraseña se ha copiado en tu portapapeles para que la puedas insertar')
    pyperclip.copy(contrasena)
    input()
    
def menu():
    while True:
        print('*' * 40 + ' MENU ' + '*' * 40)
        print('1.- Generar contraseña')
        print('2.- Generar contraseña sin numeros')
        print('3.- Generar contraseña sin c. especiales')
        print('4.- Salir')
        opcion = input('>>')

        try: 
            opcion = int(opcion)
            if opcion != 4:
                longitud = input('Ingrese el numero de caracteres de la contraseña: ')
                longitud = int(longitud)
        except Exception as e:
            print(e)
            break

        if opcion == 1:
            contrasena = gen_contrasena(longitud)
            imprimir(contrasena)
        if opcion == 2:
            contrasena = gen_contrasena_no_num(longitud)
        if opcion == 3:
            contrasena = gen_contrasena_no_esp(longitud)
        if opcion == 4:
            break
        

def main():
    menu()

if __name__ == '__main__':
    main()