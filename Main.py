import os
""" from csv import reader """
def cargar(directorio,imagen,formato):
    print("cargando "+imagen)
    """ with open(directorio+imagen, 'r') as csv_file:
        csv_reader = reader(csv_file)
        list_of_rows = list(csv_reader)
        print("imagen de " + str(len(list_of_rows))+ " x "+ str(len(list_of_rows[0]))) """

    reader = open(directorio+imagen, 'r')
    rows=reader.readlines()
    matriz_imagen=[]
    for i in rows:
        matriz_imagen.append(i.split(','))
    return matriz_imagen



def guardar():
    print("metodo por realizar")


def comprimir():
    print("metodo por realizar")

directorio = 'datasets/csv/enfermo_csv/'

lista_imagenes = os.listdir(directorio)

for imagen in lista_imagenes:
    matriz_imagen=cargar(directorio,imagen,'csv')
    print("imagen de " + str(len(matriz_imagen))+ " x "+ str(len(matriz_imagen[0])))