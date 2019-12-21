def is_prime(number):
  if number <= 1:
    return False
  for i in range(2,number):
    if number % i == 0:
      return False
  return True

def is_even(number):
  return number % 2 == 0



numbers = []
odd_numbers = []
for i in range(2, 1001):
  if is_prime(i) == False:
    numbers.append(i)
for i in numbers:
  if is_even(i) == False:
    odd_numbers.append(i)

print('El total de numeros que no son primos es {}'.format(len(numbers)))
print('El total de numeros impares es {}'.format(len(odd_numbers)))        
result = (len(odd_numbers) * 100) / len(numbers) 
print('El porcentaje de número impares es {}%'.format(round(result,1)))

#print(numbers)
