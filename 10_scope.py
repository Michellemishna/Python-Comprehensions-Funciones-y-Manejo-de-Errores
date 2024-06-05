#aqui price tiene un alcance global
price = 100
print(price)

#aqui price tiene un alcance local
def increment():
  price = 200
  price = price + 10
  print(price)
  return price
  
print(price)
price_2 = increment()
print(price_2)

#aqui price tiene un alcance global
price2 = 140
result = 200

#aqui price tiene un alcance local
def increment2():
  price_3 = 210
  result = price_3 + 10
  print(result)
  return result
print(price2)
price_4 = increment2()


#ejercicio abarca los primeros 10 temas:
def message_creator(text):
   # Escribe tu solución 👇
   text = text.lower()

   entrada = ('computadora','celular','cable')
   salida = ('Con mi computadora puedo programar usando Python','En mi celular puedo aprender usando la app de Platzi','¡Hay un cable en mi bota!')

   if text in entrada:
      return salida[entrada.index(text)]
   else: 
      return 'Artículo no encontrado'



text = 'computadora'
response = message_creator(text)
print(response)