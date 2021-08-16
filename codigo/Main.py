import os
def cargar(directorio,imagen,formato):
    print("cargando "+imagen)


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

os.chdir("C:/Users/almah/Documents/GitHub/Estructura_Datos/Código/datasets/csv/")
directorio = "enfermo_csv/"

lista_imagenes = os.listdir(directorio)

for imagen in lista_imagenes:
    matriz_imagen=cargar(directorio,imagen,'csv')
    print("imagen de " + str(len(matriz_imagen))+ " x "+ str(len(matriz_imagen[0])))