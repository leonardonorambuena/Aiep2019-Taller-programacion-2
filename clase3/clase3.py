from number_helper import NumberHelper

#for i in range(1,101):
    #if NumberHelper.is_par(i):
        #print(i)

#NumberHelper.is_prime(5)

prime_numbers = []
number = int(input('¿Ingrese cantidad de número para evaluar? '))

for i in range(number + 1):
    if NumberHelper.is_prime(i):
        prime_numbers.append(i)

print(prime_numbers)


