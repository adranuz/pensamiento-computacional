#el numero que vamos a buscar
objetivo = int(input('Escoje un numero: '))

#epsilon que es nuesto margen de error
epsilon = 0.01

#limite inferior
bajo = 0.0

# regresame el mas alto de los siguientes valores
alto = max(1.0, objetivo)

# para cortar entre dos
respuesta = (alto + bajo) / 2

#abs para obtener valores absolutos
#la resta nos da serteza que la diferencia en tre el objetivo y la respuesta es menor a el margen de error
while abs(respuesta**2 - objetivo) >= epsilon:
  print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}**2 = {respuesta**2}')
  if respuesta**2 < objetivo:
    bajo = respuesta
  else:
    alto = respuesta
  respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')