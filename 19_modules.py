# sys es una libreria que tiene varias funciones para trabajar con el sistema operativo
import sys
print(sys.path)

#re es una libreria que tiene varias funciones para trabajar con expresiones regulares
import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es 3'
result = re.findall('[0-9]+', text)
print(result)

#time es una libreria que tiene varias funciones para trabajar con horas y fechas

#time.time() devuelve el numero de segundos desde el 1 de enero de 1970
import time
timestamp = time.time()
print(timestamp)

#time.localtime() devuelve una tupla con el tiempo local
local = time.localtime()
#asctime() devuelve una cadena con el tiempo local de manera que se pueda leer
result = time.asctime(local)
print(result)

#collections es una libreria que tiene varias funciones para trabajar con listas y lo que hace es que se pueden crear listas con diferentes tipos de datos
import collections
numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3,3,21]

#aqui se crea un diccionario con la frecuencia de cada numero usando Counter hace que se pueda contar la frecuencia de cada numero
counter = collections.Counter(numbers)
print(counter)