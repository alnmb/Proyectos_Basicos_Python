import os
from pathlib import Path
import csv
import pandas as pd

registro_notas = []

def menu():
    while True:
        #Validar si existe lista y si no, crearla
        print('\n'+'*' * 45 + "  MENU " + '*' * 45)
        opcion = input('\nSeleccione del menu: \n1.Mostrar todo\n2.Agregar nota\n3.Eliminar Nota\n4.Salir\n>>')
        
        try:
            opcion = int(opcion)
            if opcion < 1 or opcion > 4:
                raise
        except Exception as e:
            os.system('clear')
            print('Ingrese un valor correcto (1,2,3,4)')
            break

        if opcion == 1:
            os.system('clear')
            mostrar_todo(registro_notas)
        if opcion == 2:
            os.system('clear')
            agregar_nota(registro_notas)
        if opcion == 3:
            os.system('clear')
            eliminar_nota(registro_notas)
        if opcion == 4:
            break

def agregar_nota(registro_notas):
    print('\n'+'*' * 40 + " Agregar Tarea " + '*' * 40)
    nombre = input('Ingrese nombre del alumno: ')
    calificacion = input('Ingrese calificacion del alumno: ')
    new_valores = (nombre, calificacion)
    registro_notas.append(new_valores)
    mostrar_todo(registro_notas)

def mostrar_todo(registro_notas):
    #print('\n'+'*' * 40 + " Completar Tarea " + '*' * 40)
    print('\nMostrando tus tareas...')
    
    for nombre, calificacion in registro_notas:
        print(f'nombre:{nombre}\ncalificacion:{calificacion}')



def eliminar_nota(registro_notas):
    print('\n'+'*' * 40 + " Eliminar Tarea " + '*' * 40)
    mostrar_todo()
    nombre = input('Ingrese nota a eliminar: ')
    calificacion = input('Ingrese calificacion a eliminar: ')

    valor = (nombre, calificacion)

    for registro in registro_notas[:]:  # Creating a copy of the list to avoid modifying it while iterating
        if registro == valor:
            registro_notas.remove(registro)

def main():
    menu()



if __name__ == '__main__':
    main()