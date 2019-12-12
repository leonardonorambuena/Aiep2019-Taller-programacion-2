import random

assert_number = False
number_random = random.randint()

while assert_number == False:
    number = int(input('Ingrese un numero entre 1 y 15  '))

    if number_random == number:
        print('Felicidades {} es el numero correcto'.format(number))
        assert_number = True
    else:
        print('Lo siento {} no es el correcto'.format(number))

    if number_random > number:
        print('El número correcto es mayor al ingresado')

    if number_random < number:
        print('El número correcto es menor al ingresado')