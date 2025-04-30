import unittest
from src.calculator import sum, subtract, multiplication, division

"""
Esta clase nos va a dar una serie de funcionalidades que nos van a permitir ver el progreso de 
las pruebas, qué prueba se ejecutó, qué prueba falló, por qué falló
"""
class CalculatorTest(unittest.TestCase):
    
    def test_sum(self):
        assert sum(2, 3) == 5
   
    def test_subtract(self):
        assert subtract(10, 5) == 5
   
    def test_multiplication(self):
        assert multiplication(2, 4) == 8
    
    def test_division(self):
        assert division(30, 2) == 15
    
 #   def test_division_by_zero(self):
 #       with self.assertRaises(ZeroDivisionError):
 #           division(30, 30)
