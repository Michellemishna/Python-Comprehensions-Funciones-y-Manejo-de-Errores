def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

result = find_volume(10, 20, 3)
print(result)

result2, width, text  = find_volume(width=10)
print(result2)
print(width)
print(text)


result3 = find_volume(width=10)
print(result3[0])
