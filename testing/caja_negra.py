#libreria de python para pruebas
import unittest

def suma(num_1, num_2):
  return abs(num_1) + num_2

#TDD = escribir las pruebas y luego el algoritmo que las pasa
class CajaNegraTest(unittest.TestCase):

  def test_suma_dos_positivos(self):
    num_1 = 10
    num_2 = 5

    resultado = suma(num_1, num_2)
    self.assertEqual(resultado, 15)

  def test_resta_dos_negativos(self):
    num_1 = -10
    num_2 = -7

    resultado = suma(num_1, num_2)
    self.assertEqual(resultado, -17)

#esta linea checa el test
if __name__ == '__main__':
  unittest.main()