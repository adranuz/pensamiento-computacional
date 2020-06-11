#Este programa agrega todos los anteriores, los mete cada uno en una funcion y despues los da a elejir
print('Este programa permite sacar raices cuadradas.') 
el_numero = int(input('Escoge un entero para sacarle la raiz: '))
print('Estas son las opciones para sacar tu raiz: ')
print('- Ingresa 1 para la Enumeracion Exahustiva.')
print('- Ingresa 2 para la Aproximacion epsilon.')
print('- Ingresa 3 para la Busqueda Binaria.')
opcion = int(input('Ingresa tu opcion y da enter: '))




# Enumeracion exahustiva
def exahustiva(objetivo):
  #objetivo = int(input('Escoge un entero: '))
  respuesta = 0

  while respuesta**2 < objetivo:
    print(respuesta, respuesta**2)
    respuesta += 1

  if respuesta**2 == objetivo:
    return print(f'La raiz cuadrada de {objetivo} es {respuesta}')
  else:
    return print(f'{objetivo} no tiene una raiz cuadrada exacta')

# Aproximacion
def aproximacion(objetivo):
  #objetivo = int(input('Escoge un entero: '))
  epsilon = 0.01 # rango de acercamiento a la verdad
  paso = epsilon**2 #0.001
  respuesta = 0.0

  while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(respuesta)
    respuesta += paso

  if abs(respuesta**2 - objetivo) >= epsilon:
    return print(f'No se encontró la raiz cuadrada de {objetivo}')
  else:
    return print(f'La raiz de {objetivo} es {abs(respuesta)}')

# Busqueda binaria
def binaria(objetivo):
  #objetivo = int(input('Escoje un numero: '))
  epsilonon = 0.01 
  bajo = 0.0 
  alto = max(1.0, objetivo) 
  respuesta = (alto + bajo) / 2 

  while abs(respuesta**2 - objetivo) >= epsilonon:
	  print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}**2 = {respuesta**2}')
	  if respuesta**2 < objetivo:
		  bajo = respuesta
	  else:
		  alto = respuesta
	  respuesta = (alto + bajo) / 2
  return print(f'La raiz cuadrada de {objetivo} es {respuesta}')


if (opcion == 1):
  exahustiva(el_numero)
elif (opcion == 2):
  aproximacion(el_numero)
elif (opcion == 3):
  binaria(el_numero)
else: 
  print('Aun no tenemos esa opcion. Vuelve pronto.')