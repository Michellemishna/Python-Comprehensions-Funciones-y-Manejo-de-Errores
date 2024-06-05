#r+ sirve para leer y escribir en el archivo manteniendo el contenido

with open( './text.txt','r+') as file:
  for line in file:
    print(line)
  file.write( 'nuevas cosas en este archivo\n')
  file.write( 'otra linea\n')

#w+ sirve para leer y escribir en el archivo pero en este caso sobreescribe el contenido cada vez que se ejecute el programa
with open( './text.txt','w+') as file:
  for line in file:
    print(line)
  file.write( 'nuevas cosas en este archivo\n')
  file.write( 'otra linea\n')


# ejercicio csv archivo main
import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path,'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      total = sum([int(line[1]) for line in reader])
   return total

response = read_csv('./data.csv')
print(response)

#archivo data
Administration,200
Marketing,201
Purchasing,114
Human Resources,203
Shipping,121
IT,103
Public Relations,204
Sales,145
Executive,100
Finance,108