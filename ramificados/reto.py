# Reto, pedir nombre y edad de dos personas, compararlos y decir cual es el mayor

user_1 = str(input('Introduce tu nombre: '))
edad_1 = int(input('Introduce tu edad: '))


user_2 = str(input('Introduce el nombre de la persona mas cercana: '))
edad_2 = int(input('Introduce su edad: '))

if edad_1 > edad_2: 
  print(f'El usuario {user_1} es mayor que {user_2}')
elif edad_1 < edad_2: 
  print(f'El usuario {user_1} es menor que {user_2}')
else:
  print('Los dos tienen la misma edad')