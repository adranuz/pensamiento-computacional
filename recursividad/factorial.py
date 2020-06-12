def factorial(numero):
  """Calcula el factorial de numero

  numero int > 0 
  returns n!
  """
  if numero == 1:
    return 1

  return numero * factorial(numero -1)

numero = int(input('Escribe un numero entero: '))

print(factorial(numero))