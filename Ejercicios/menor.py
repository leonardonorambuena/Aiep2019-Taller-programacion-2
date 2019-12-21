numbers = []
for i in range(1, 11):
  numbers.append(int(input('Ingrese el valor {} '.format(i))))


ordened_numbers = sorted(numbers)

print('El numero menor es {}'.format(ordened_numbers[0]))