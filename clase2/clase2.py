def run():
  a = input('Cual es tu nombre? ')
  b = input('Cual es su apellido ')
  c = int(input('Ingrese su edad '))
  print('Bienvenido {} {} su edad es {}'.format(a, b, c))


if __name__ == '__main__':
  run()