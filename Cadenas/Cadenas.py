#Consulta e Información
cadena="Murcielago"
lista=["1","2","3"]
len(cadena) #Longitud de la cadena
cadena.isalpha() #True o false, solo letras
cadena.isdigit() #Solo digitos
cadena.isalnum() #Letras y/o numeros
cadena.isspace() #Solo espacios en blanco
cadena.islower() #Minusculas
cadena.isupper() #Mayusculas
cadena.startswith("M") #Empieza con...
cadena.endswith("O") #Termina con...

#Transformacion
cadena.upper() #MAYUS
cadena.lower() #minus
cadena.capitalize() #Capitaliza
cadena.title() #Cada Palabra Con Mayúscula
cadena.swapcase() #Cambia mayúsculas con minúsculas y viceversa
cadena.strip() #Elimina espacios al inicio y al final
cadena.lstrip() #Elimina espacios a la izq
cadena.rstrip() #Elimina espacios a la der
cadena.replace("o","a") #Cambia todas las o por a

#Búsqueda
cadena.find("c") #Primera aparición de la letra o palabra. retorna el índice, lanza -1 si no está
cadena.rfind("g") #Ultima aparación.
cadena.index("r") #Lo mismo que find pero lanza error si no lo encuentra
cadena.count("a") #Cuenta cuántas veces aparece a

#División y unión
cadena.split("i") #Retorna una lista separada por i
cadena.rsplit("i") #Divide desde la derecha, solo hay diferencia cuando se utiliza un segundo atribut "maxsplit", ej: uno-dos-tres-cuatro con rsplit("-") es uno-dos,tres,cuatro
cadena.rpartition("i") #Desde la der
cadena.partition("i") #tupla. Ej: "nombre:apellido:edad" -> ('nombre',':','apellido:edad')
"sep".join(lista) #Une elementos de una lista con un separador, retorna un string

#Alineacion y formato
cadena.center("ancho","relleno") #Centra con relleno
cadena.ljust("ancho", "relleno") #Alinea a la izq
cadena.rjust("ancho","derecho") #Alinea a la derecha
cadena.zfill("ancho") #Rellena con ceros a la izquierda
format() #formatea valores

#Otras
ord("c") #Código unicode del carácter
chr("codigo") #Caracter a partir del código unicode
cadena.encode() #Codifica a bytes
cadena.casefold() #Versión insensible a mayúsculas/minúsculas (otros idiomas)"""