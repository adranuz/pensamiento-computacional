# objetivo, ver si el numero ingresado tiene una raiz cuadrada exacta

objetivo = int(input('Escoge un entero: '))
respuesta = 0

# Respuesta se multiplicará por sí misma hasta que tenga un valor que no sea menor al objetivo, que será cuando se pare el programa obtenga la respuesta
while respuesta**2 < objetivo:
  print(respuesta, respuesta**2)
  respuesta += 1

# Una vez cumpliendoce la aproximacion de respuesta veremos si es o no exacta
if respuesta**2 == objetivo:
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
  print(f'{objetivo} no tiene una raiz cuadrada exacta')