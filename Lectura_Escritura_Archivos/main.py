import os
import csv
import pandas as pd
import datetime


def validar_archivo():
    lista = 'eventos.csv'
    file = 'Lectura_Escritura_Archivos/archivo/eventos.csv'

    if os.path.exists(file):
        #print(f"El archivo {lista} existe.")
        return file
    else:
        #print(f"El archivo {lista} no existe.")
        #print('Creando lista')
        with open(file, 'w', newline='') as archivo:
            encabezados = ["timestamp", "nombre", "descripcion"]
            escritor = csv.writer(archivo)
            escritor.writerow(encabezados)  
        return file
    
def visualizar_eventos(archivo):
    print('\n'+'*' * 40 + " Visualizar Eventos " + '*' * 40)
    csv = pd.read_csv(archivo)
    if csv.empty:
        print('el archivo está vacio')
    else: 
        print(csv)

def registrar_eventos(archivo):
    print('\n'+'*' * 40 + " Agregar Evento " + '*' * 40)
    csv = pd.read_csv(archivo)
    fecha_actual = datetime.datetime.now()
    formatted_fecha = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")

    nombre = input('¿Cual es el nombre de su evento?\n>>')
    add_desc = input('Desea agregar descripcion? (Y or N)\n>>')
    if add_desc.upper() == 'Y':
        descripcion = input('¿Cual es la descripcion de su evento?\n>>')
    else:
        descripcion = ''

    df = pd.DataFrame({'timestamp':[formatted_fecha],
                       'nombre':[nombre],
                       'descripcion':[descripcion]})
    df.to_csv(archivo,mode='a', index=False, header=False)

def menu(archivo):
    while True: 
        print('*' * 40 + ' MENU ' + '*' * 40)
        print('1. Mostrar Eventos Registrados')
        print('2. Registar nuevo evento')
        print('3. Salir')

        opcion = input('>>')

        if opcion == '3':
            break
        else:
            try:
                opcion = int(opcion)
            except Exception as e:
                print(e)
                break
        if opcion == 1:
            visualizar_eventos(archivo)
        elif opcion == 2:
            registrar_eventos(archivo)
        else:
            print('Opcion no valida, ingrese una de las especificadas')

def main():
    archivo = validar_archivo()
    menu(archivo)

if __name__ == '__main__':
    main()