#como leer un archivo
file = open('./text.txt')
print(file.read())

#como leer un archivo linea por linea
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

#como leer un archivo linea por linea y cerrar el archivo
for line in file:
  print(line)

#para cerrar el archivo dandole la indicaion de que se cierre
#file.close()

#usamos with para no tener que cerrar el archivo, lo cierra automaticamente
with open('./text.txt') as file:
  for line in file:
    print(line)

