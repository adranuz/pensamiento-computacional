x = 0.0

for i in range(10):
  x += 0.1 #esto deberia dar 1

if x == 1.0:
  print(f'x = {x}')
else: 
  print(f'x != {x}') #pero da 0.999999999