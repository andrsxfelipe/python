#Listas

##Creación y conversión
lista=[]
list(iterable) #Cadena o tupla

##Agregar
lista.append(elem=1) #Agrega al final 1
lista.insert(pos=0,elem=1) #Agrega en la posición 0 el 1 y corre el resto
lista.extend(l2=[1,2,3]) #Agrega varios elementos de otra lista

##Eliminar
lista.remove(elem=1) #Elimina la primera aparicion del elemento
lista.pop([1]) #ELimina y retorna el elemento en pos, por defecto es el último
del lista[1] #Elimina el elemento en esa posición
lista.clear() #Vacía la lista

##Consulta y búsqueda
elem="p" in lista #Verifica si el elemento está en la lista
lista.index(elem=1) #Devuelve la posición del primer elem
lista.count(elem=1) #Cuántas veces aparece

##Orden y reversa
lista.sort() #Ordena de menor a mayor
lista.sort(reverse=True) #Ordena de mayor a menor
lista.reverse() #invierte el orden actual
sorted(lista) #Devuelve una nueva lista ordenada sin modificar la orginal

##Otra
len(lista) #Cantidad de elementos
min(lista),max(lista),sum(lista) #Mínimo máximo y suma
lista.copy() #Copia superficial de la lista
list(reversed(lista)) #Devuelve una lista invertida, no modifica la original
enumerate(lista) #Devuelve pares (índice, valor) al iterar
zip(lista,l2) #Ejemplo nombres=[Ana, Felip] edades=[20,23] despues del zip: [(Ana,20),(Felipe,23)]

##Función últil con listas: map()
###Es usada cuando quieres aplicar una misma función a todos los elementos de una lista o iterable *sin escribir un bucle*
map(funcion=int, iterable=lista) #Convierte todos los elementos en enteros
###Fucionada con lambda
list(map(lambda x: x**2, lista)) #Eleva todos los valores al cuadrado

##Funcion filter()
###Filtrar elementos de un iterable que cumplan una condicion, retorna True o False para cada elemento, devuelve un iterador, usualmenter list() para devolverla
###Ejemplo:
numeros=[1,2,3,4,5,6]
pares=list(filter(lambda x:x%2==0, numeros)) #[2,4,6]

##Funcion reduce() (requiere importarlo)
###Sintaxis
####from functools import reduce
####reduce(funcion,iterable)

suma=reduce(lambda x,y:x+y, numeros,10) #EL ultimo parametro es para que el acumulador (x) empiece en 10, si no se indica, se toma el primer valor del la lista

#Tuplas
##Crear
tupla=(1,2,3)
tupla2=tuple([4,5,6])