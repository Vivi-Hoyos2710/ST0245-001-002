#ADVERTENCIA: El codigo lo habiamos puesto en el repositorio antes de organizarlo en la carpeta correspondiente, al ponerlo en la carpeta código no corre, pero por fuerande ella si (la parte principal del repositorio). 
#Problemas al correr en visual studio code.
import os
def cargar(directorio,imagen,formato):
    print("cargando "+imagen+"como formato "+formato)
  

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


directorio = 'codigo/datasets/csv/enfermo_csv/'#carpeta de los animales enfermos

lista_imagenes = os.listdir(directorio)

for imagen in lista_imagenes:
    matriz_imagen=cargar(directorio,imagen,'csv')
    print("imagen de " + str(len(matriz_imagen))+ " x "+ str(len(matriz_imagen[0])))

directorio = 'codigo/datasets/csv/sano_csv/'#carpeta de los animales sanos

lista_imagenes = os.listdir(directorio)

for imagen in lista_imagenes:
    matriz_imagen=cargar(directorio,imagen,'csv')
    print("imagen de " + str(len(matriz_imagen))+ " x "+ str(len(matriz_imagen[0])))