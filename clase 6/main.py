import random
import datetime

option = 's'
numbers = []
while option.lower() != 'n':
  user_result = 0
  try_user = 0
  number = random.randint(1, 15)
  result = number ** 2
  first_time = datetime.datetime.now()
  while result != user_result:
    user_result = int(input('indique {} al cuadrado '.format(number)))
    try_user = try_user + 1
    if user_result < result:
      print('El resultado es mayor al ingresado')
    if user_result > result:
      print('El resultado es menor al ingresado')
  last_time = datetime.datetime.now()
  seconds = last_time - first_time
  total_seconds = round(seconds.total_seconds())
  numbers.append(total_seconds)
  print('Felicidades has acertado en el resultado en {} segundos y en {} intentos '.format(total_seconds, try_user))
  option = input('Desea voler a jugar s/n ')
if len(numbers) > 1:
  number_sorted = sorted(numbers)
  lower_time = number_sorted[0]
  count_game = len(numbers)

  print('Has jugado {} veces y tu mejor tiempo fue {} segundos'.format(count_game, lower_time))
    

  





