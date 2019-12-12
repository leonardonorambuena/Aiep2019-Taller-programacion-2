def init():
  number = int(input('Ingrese un número '))
  x = 0
  str_numbers = ''
  for i in range(1,number + 1):
    if i % 2 == 0:
      x = x + 1
      str_numbers = str_numbers + '|'+ str(i)
  print('La cantidad de números pares es {}'.format(x))

  print('Los numeros pares son {}'.format(str_numbers))

if __name__ == "__main__":
    init()