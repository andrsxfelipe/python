#1. Abrir y cerrar archivos
archivo = open('Nombre_archivo.txt','modo') #En modo puede ir a, que significa append; r, lectura; w, escritura; b, modo binario (ejemplo 'rb', 'wb')

#2. Leer archivos
contenido = archivo.readline() #Lee solo una línea. Útil para archivos .csv o .txt si tienen un encabezado
contenido = archivo.readlines() #Lee todas las líneas
contenido = archivo.read()  #Lee todo el archivo

#3. Escribir y añadir contenido
archivo.write('')

#4. Usar with para manejo automático
with open('nuevo.txt','r') as archivo:
    for linea in archivo:
        print(linea.strip())

#5. Trabajar con archivos como listas
with open('nuevo.text', 'r') as archivo:
    lineas = archivo.readlines()
    #Todo lo que esté dentro de la identación es lo que se hará con el archivo, una vez se salga de la identación el archivo estará cerrado

lineas[0]='Linea modificada\n'

with open('nuevo.txt','w') as archivo:
    archivo.writelines(lineas)

#6. Comprobar si un archivo existe
import os
if os.path.exists('nuevo.txt'):
    print('El archivo existe')
else:
    print('No existe')

#7. Lectura y escritura de archivos CSV
import csv

#7.1 Leer
with open('datos.csv','r', newline='') as archivo:
    lector = csv.reader(archivo) #Lee el archivo como lista de filas
    for fila in lector: #Cada fila es una lista con los valores separados por comas
        print(fila)

#7.2 Escribir
with open('salida.csv','w', newline='') as archivo: #newline evita lineas en blanco en windows
    escritor = csv.writer(archivo)
    escritor.writerow(['Nombre','Edad','Pais']) #Escribe una fila
    escritor.writerow(['Carla','28','Argentina'])
    escritor.writerow(['Juan','35','Perú'])

#7.3 Leer con encabezados usando DictReader
with open('datos.csv','r',newline='') as archivo:
    lector = csv.DictReader(archivo) #DictReader convierne cada fila en un diccionario, usando la primera fila como claves
    for fila in lector:
        print(fila['NOmbre'],fila['País'])

#7.4 Escribir usando DictWriter
with open('nuevos_datos.csv','r',newline='') as archivo:
    campos = ['Nombre','Edad','País']
    escritor = csv.DictWrite(archivo, fieldnames=campos)

    escritor.writeheader()
    escritor.writerow({'Nombre':'Luis','Edad':29,'Pais':'Chile'})
    escritor.writerow({'Nombre':'María','Edad':24,'Pais':'Uruguay'})


#8. Manejo de archivos .json
#9. Archivos binarios
#10. Gestión errores con try/except