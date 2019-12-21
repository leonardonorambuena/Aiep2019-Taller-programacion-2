def validateRut(rut):
  dv = rut[len(rut)-1]
  numbers_list = [int(i) for i in rut[:-1] if i.isdigit()]
  m = 2
  result = 0
  for i in numbers_list[::-1]:
    result = result + (m * i)
    m = m + 1
    if (m == 8):
      m = 2
  dv_calculated = 11 - (result % 11)
  if (dv_calculated == 11 and dv == '0'):
    return True
  if (dv_calculated == 10 and dv.upper() == 'K'):
    return True
  return dv.isdigit() and dv_calculated == int(dv)

rut = input('Ingrese su rut: ')

if (validateRut(rut) == True):
  print('El rut es correcto')
else:
  print('El rut es incorrecto')






