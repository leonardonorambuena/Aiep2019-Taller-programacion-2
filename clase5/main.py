def run(rut):
  last_index = len(rut) - 1
  dv = rut[last_index]
  numbers = []

  for i in range(last_index):
    if rut[i].isdigit():
      numbers.append(int(rut[i]))
  m = 2
  result = 0
  for i in range(len(numbers) - 1,-1,-1):
    result = result + (m * numbers[i])
    m = m + 1
    if m == 8:
      m = 2
  dv_calculated = 11 - (result % 11)
  if dv_calculated == 11 and dv == '0':
    return True
  if dv_calculated == 10 and dv.lower() == 'k':
    return True

  return str(dv_calculated) == dv

  print(dv_calculated)

if __name__ == '__main__':
  is_valid = False

  while is_valid == False:
    rut = input('Ingrese su Rut: ')
    if run(rut) == True:
      print('Rut Correcto')
      is_valid = True
    else:
      print('Rut incorrecto')