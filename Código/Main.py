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

ubicacion = input("Inserte el directorio donde están las carpetas de enfermo_csv y sano_csv, P.D: Cambiar los \ por /")
os.chdir(ubicacion)
directorio = 'enfermo_csv/'
directorio2= 'sano_csv/'

lista_imagenes_Enfermos = os.listdir(directorio)
lista_imagenes_Sanas = os.listdir(directorio2)

for imagen in lista_imagenes_Enfermos:
    matriz_imagen=cargar(directorio,imagen,'csv')
    print("imagen de " + str(len(matriz_imagen))+ " x "+ str(len(matriz_imagen[0])))
    
for imagen in lista_imagenes_Sanas:
    matriz_imagen=cargar(directorio,imagen,'csv')
    print("imagen de " + str(len(matriz_imagen))+ " x "+ str(len(matriz_imagen[0])))