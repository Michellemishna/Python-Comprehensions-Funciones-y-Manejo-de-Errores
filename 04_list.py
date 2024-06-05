numbers = []

for element in range(1, 11):
  numbers.append(element)
print(numbers)

# List Comprehension
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

# List Comprehension con condicion
numbers2 = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers2.append(i * 2)
print(numbers2)

# List Comprehension con condicion ya dentro de la lista
numbers_v3 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v3)

