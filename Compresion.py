import os
import string
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve
espacioTrabajo = os.getcwd()
import time
import timeit
from collections import deque
class Imagen:
    nombre = None  # Nombre archivo de la imagen
    ubicacion = None  # Direccion en la que se halla la imagen
    matriz_bytes = None  # Matriz de numpy que contiene bytes de cada imagen

    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.matriz_bytes = None

    def generar_ubicacion(self, nueva_ubicacion: str):
        self.ubicacion = nueva_ubicacion

    def calculo_energia(self):
        filtro_horizontal = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        filtro_vertical = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        # Se aplica la convulución respecto a los filtros.
        convol_horizontal = convolve(self.matriz_bytes, filtro_horizontal)
        convol_vertical = convolve(self.matriz_bytes, filtro_vertical)
        # Esta operacion nos devuelve un mapa de energia para matrices con valores en escala de grises.
        return np.absolute(convol_horizontal) + np.absolute(convol_vertical)

    def cargarImagen(self):
        print("cargando... "+self.nombre+" como formato cvs")
        reader = open(self.ubicacion+self.nombre, 'r')
        self.matriz_bytes = np.loadtxt(reader, delimiter=",")

    def mostrarImagen(self):
        plt.figure(figsize=(10, 10))
        plt.grid("off")
        plt.axis("off")
        # Recibe la matriz de cada imagen en bytes con valores de 0 a 255.
        plt.imshow(self.matriz_bytes, cmap="gray", vmin=0, vmax=255)
        plt.show()

    def minimaCostura(self):
        r, c = self.matriz_bytes.shape
        mapaEnergia = self.calculo_energia()
        M = mapaEnergia.copy()
        retroceso = np.zeros_like(M, dtype=np.int)
        for i in range(1, r):
            for j in range(0, c):
                if j == 0:
                    idx = np.argmin(M[i - 1, j:j + 2])
                    retroceso[i, j] = idx + j
                    min_energy = M[i - 1, idx + j]
                else:
                    idx = np.argmin(M[i - 1, j - 1:j + 2])
                    retroceso[i, j] = idx + j - 1
                    min_energy = M[i - 1, idx + j - 1]
                M[i, j] += min_energy
        return M, retroceso

    def cortarColumna(self):
        r, c = self.matriz_bytes.shape
        M, retroceso = self.minimaCostura()
        filtro = np.ones((r, c), dtype=np.bool)
        j = np.argmin(M[-1])
        for i in reversed(range(r)):
            filtro[i, j] = False
            j = retroceso[i, j]
        self.matriz_bytes = self.matriz_bytes[filtro]
        self.matriz_bytes = self.matriz_bytes.reshape(r, c-1)

    def cortarFila(self, scale):
        self.matriz_bytes = np.rot90(self.matriz_bytes, 1)
        self.eliminandoColumnas(scale)
        self.matriz_bytes = np.rot90(self.matriz_bytes, 3)
    @profiler
    def eliminandoColumnas(self, scale_c):
        
        r, c = self.matriz_bytes.shape
        new_c = int(scale_c * c)
        for i in range(c - new_c):
            
            self.cortarColumna()

    def resumirImagen(self):
        r, c = self.matriz_bytes.shape
        for i in range(r):
            for j in range(c):
                self.matriz_bytes[i][j] = (self.matriz_bytes[i][j]//50)*50

    def recorridoLongitudCompresion(self):
        Datos = [] #datos comprimidos no se puede dque por el metodo que se esta usamdo para guardar la matriz
        for i in range(len(self.matriz_bytes)): #cyclo para recorrer filas de la matriz
            Estamos = self.matriz_bytes[i]#señalar la matriz original
            n = len(Estamos)
            j= 0
            SalidaDeLaFila = []#arreglo para guar la salida de cada fila
            while j<= n - 1: #ciclo para recorrer todos los caracteres
                contador = 1
                while (j< n - 1 and Estamos[j] == Estamos[j+ 1]):#ciclo para contar los caracteres repetidos
                    contador += 1
                    j+= 1
                j+= 1#se suma despes de terminar el ciclo para iniciar el proximo desde un caracter nuevo
                
                if contador > 1:
                    SalidaDeLaFila.append("$"+str(contador)) #añadir repeticiones silas hay
                SalidaDeLaFila.append(Estamos[j- 1])  #añadir el caracter
            
            Datos.append(SalidaDeLaFila)#guerdar en la matriz

        return Datos

def guardarImagenComprimida(matriz,imagen,carpeta):
    np.savetxt("codigo/datasets/csv/"+carpeta+"/ImagenComprimida" + str(imagen.nombre), matriz,fmt='%s', delimiter=",")
def descomprimirRecorridoDeLongitud(imagen):
    
    nuevaImagen=[]
    for i in range(len(imagen)):
        estamos=imagen[i]
        n=len(estamos)
        salida_de_linea=[]
        j=0
        while j<n:
            repetir=str(estamos[j])
            if repetir[0]=='$':
                rellenar=int(float(estamos[j+1]))
                repetir=int(repetir[1:])
                for k in range(repetir):
                    salida_de_linea.append(rellenar) 
                j+=1
            else:
                salida_de_linea.append(int(float(repetir)))
            j+=1
        nuevaImagen.append(salida_de_linea)
    return nuevaImagen
class Main:
    directorioActual =  espacioTrabajo.replace(string.punctuation[23], string.punctuation[14]) #Directorio actual reemplazando "\" por "/"
    lista_imagenes_Enfermos = os.listdir(directorioActual+'/codigo/datasets/csv/enfermo_csv/')#cambiar enfermo_csv por enfermo_csv
    lista_imagenes_Sanos= os.listdir(directorioActual+'/codigo/datasets/csv/sano_csv/')
    #Cargando imagenes de animales enfermos
    c=0
    listaTiempos2=deque()
    for imagen in lista_imagenes_Sanos:
         
        img=Imagen(imagen,directorioActual+'/codigo/datasets/csv/sano_csv/')#cambiar zzz por enfermo_csv
        img.cargarImagen()
        tamanyooriginal=os.path.getsize(img.ubicacion+imagen)
        #imagenEnfermo.mostrarImagen()
        start1 = time.time()
        #start2=timeit.timeit()
        ejecutarSeamCarving(img)
        #plt.figure(figsize=(10, 10))
        #plt.grid("off")
        #plt.axis("off")
            # Recibe la matriz de cada imagen en bytes con valores de 0 a 255.
        #plt.imshow(img.calculo_energia(), cmap="gray", vmin=0, vmax=255)
        #plt.show()
        
        img.eliminandoColumnas(0.98)
        end1 = time.time() #Termina seamm carving
        ejecucionSeam=end1-start1
        #img.cortarFila(0.7)
        #img.mostrarImagen()
        print("Con seam carving")
        print(img.matriz_bytes)
        start2= time.time()
        img.resumirImagen()
        #print("resumiendo: ")
        #print(img.matriz_bytes)
        #img.mostrarImagen()
        decodificado=img.recorridoLongitudCompresion()
        end2=time.time()
        #end2=timeit.timeit()
        tiempoEjecucion=end2 - start2
        guardarImagenComprimida(decodificado,img,"sanoComprimido")
        tamanyoComprimido=os.path.getsize("codigo/datasets/csv/sanoComprimido/ImagenComprimida" + imagen)
        totalComprimido=tamanyooriginal-tamanyoComprimido 
        
        #nombreimagen,tiempo ejecucion de compresion,toriginal, tcomprimido
        listaTiempos2.append((imagen+","+str(tamanyooriginal)+","+str(ejecucionSeam)+","+str(tiempoEjecucion)+","+str(tamanyoComprimido)+","+str(totalComprimido)))
        #print("con timeit")
        #print(end2 - start2)          
        #print(decodificado)
        #descomp=descomprimirRecorridoDeLongitud(decodificado)
        #print(descomprimirRecorridoDeLongitud(decodificado))
        #plt.figure(figsize=(10, 10))
        #plt.grid("off")
        #plt.axis("off")
        # Recibe la matriz de cada imagen en bytes con valores de 0 a 255.
        #plt.imshow(descomp, cmap="gray", vmin=0, vmax=255)
        #plt.show()
        guardarImagenComprimida(decodificado,img,"sanoComprimido")
        
        
        
        c+=1
        if c==2:
            break
    archivoTiempo= open("datosRun.txt","w")
    archivoTiempo.write("nombreImagen,tamanyoOriginal,tEjecucionSeam,tEjecucionRun, tComprimido,totalComprimido"+"\n")
    for linea in listaTiempos2:
        archivoTiempo.write(linea+"\n")
    
    archivoTiempo.close()  