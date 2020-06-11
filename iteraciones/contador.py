
contador_externo = 0
contador_interno = 0

while contador_externo < 5:
  print('Contador externo:',contador_externo)
  while contador_interno <5:
    print('interno:', contador_interno)
    contador_interno += 1
    if contador_externo >= 3: 
      break
  contador_externo += 1
  contador_interno = 0