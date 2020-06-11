# objetivo, vamos a obtener un numero para sacarle la raiz

objetivo = int(input('Escoge un entero: '))
epsilon = 0.01 # rango de acercamiento a la verdad
paso = epsilon**2 #0.001
respuesta = 0.0

# Respuesta se multiplicará por sí misma hasta que tenga un valor que no sea menor al objetivo, que será cuando se pare el programa obtenga la respuesta
# abs nos permite mantener los margenes de numeros normales y no los combertidos de binarios, es 
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
  print(respuesta)
  respuesta += paso

# Una vez cumpliendoce la aproximacion de respuesta veremos si es o no exacta
if abs(respuesta**2 - objetivo) >= epsilon:
  print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
  print(f'La raiz de {objetivo} es {abs(respuesta)}')