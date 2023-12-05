import os
from pathlib import Path
import csv
import pandas as pd

def menu(archivo):
    while True:
        #Validar si existe lista y si no, crearla
        print('\n'+'*' * 45 + "  MENU " + '*' * 45)
        opcion = input('\nSeleccione del menu: \n1.Agregar Tarea\n2.Completar tarea\n3.Eliminar Tarea\n4.Visualizar Tareas\n5.Salir\n>>')
        
        try:
            opcion = int(opcion)
            if opcion < 1 or opcion > 5:
                raise
        except Exception as e:
            os.system('clear')
            print('Ingrese un valor correcto (1,2,3,4 o 5)')
            break

        if opcion == 1:
            os.system('clear')
            agregar_tarea(archivo)
        if opcion == 2:
            os.system('clear')
            marcar_completada(archivo)
        if opcion == 3:
            os.system('clear')
            eliminar_tarea(archivo)
        if opcion == 4:
            os.system('clear')
            visualizar_lista(archivo)
        if opcion == 5:
            break
    

def validar_lista():
    lista = 'lista.csv'
    file = 'To-do_list/lista/lista.csv'

    if os.path.exists(file):
        print(f"El archivo {lista} existe.")
        return file
    else:
        print(f"El archivo {lista} no existe.")
        print('Creando lista')
        with open(file, 'w', newline='') as archivo:
            encabezados = ["Tarea", "Status"]
            escritor = csv.writer(archivo)
            escritor.writerow(encabezados)  
        return file

def agregar_tarea(archivo):
    print('\n'+'*' * 40 + " Agregar Tarea " + '*' * 40)
    nombre_tarea = input('\nIngrese el nombre de su tarea >> ')
    with open(archivo, 'a', newline='') as csvfile:
        fieldnames = ["Tarea", "Status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Tarea': f'{nombre_tarea}', 'Status': 'Abierto'})
    
    os.system('clear')
    visualizar_lista(archivo)

def marcar_completada(archivo):
    print('\n'+'*' * 40 + " Completar Tarea " + '*' * 40)
    print('\nMostrando tus tareas...')
    visualizar_lista(archivo)

    tarea = input('\nIngrese el nombre de su tarea a completar >> ')
    print('\n')
    
    csv = pd.read_csv(archivo)
    try: 
        csv.loc[csv['Tarea'] == tarea, 'Status'] = 'Cerrado'
        csv.to_csv(archivo, index=False)
        os.system('clear')
        visualizar_lista(archivo)
    except Exception as e:
        print(e)


def eliminar_tarea(archivo):
    print('\n'+'*' * 40 + " Eliminar Tarea " + '*' * 40)
    print('\nMostrando tus tareas...')
    visualizar_lista(archivo)
    tarea = input('\nIngrese el nombre de su tarea a completar >> ')
    print('\n')

    csv = pd.read_csv(archivo)
    try: 
        csv = csv[csv['Tarea'] != tarea]
        csv.to_csv(archivo, index=False)
        os.system('clear')
        visualizar_lista(archivo)
    except Exception as e:
        print(e)
    

    

def visualizar_lista(archivo):
    print('\n'+'*' * 40 + " Visualizar Tarea " + '*' * 40)
    csv = pd.read_csv(archivo)
    print(csv)

def main():
    archivo = validar_lista()
    menu(archivo)



if __name__ == '__main__':
    main()