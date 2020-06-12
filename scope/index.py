#ejemplo de scope
# Igual que JS primero se hace un escaneo de todas las funciones y variables
# Despues corre de arriba hacia abajo 

#una manera facil de identificar el camino del codigo es ver donde se ejecuta cada funcion

#contexto global contiene
# - un_arg, cualquier_func y func1(un_arg, cualquier_func)
#es decir una variable, dos funciones, la declaracion de una de las dos funciones, con la variable y la otra funcion como argumentos
#es decir que lo primero que va a hacer el programa es ver que hay dos funciones ahi, una variable e inmediatamente va a correr la funcion  func1 con un_arg y cualquier_func como argumentos, es decir que esas dos cosas son lansadas al siguiente scope, al scope de func1

# func1 es un scope en el que para empezar tenemos dos argumentos que ya tienen contenido y que se pueden usar en cualquier lugar del scope que es un_arg = 1 y una_func = cualquier_func
#las siguientes lineas son la declaracion de func2 
#despues esta valor que obtiene el valor regresado de func2 al correrse, que su argumento seria un_arg = 1, por lo que valor = 2
#se corre una_func(valor) que valor = 2 y recordemos que una_func = cualquier_func, por lo que corremos la funcion contenida por cualquier_arg. Por lo qe lo que regresa func1 es 2 + 5 = 7
def func1(un_arg, una_func):
	def func2(otro_arg):
		return otro_arg * 2

  valor = func2(un_arg) #ejecucion 2
  return una_func(valor) #ejecucion 3

un_arg = 1 

def cualquier_func(cualquier_arg):
  return cualquier_arg + 5

func1(un_arg, cualquier_func) #ejecucion 1