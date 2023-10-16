import unittest
import NumeroMaximo

class TestMCD(unittest.TestCase):        
    def test_TC1(self): self.assertEqual(NumeroMaximo.NumeroMax(5, 4, 3), ("El valor máximo es 5 y se encuentra en la variable 'x'"))
    def test_TC2(self): self.assertEqual(NumeroMaximo.NumeroMax(3, 4, 6), ("El valor máximo es 6 y se encuentra en la variable 'z'"))
    def test_TC3(self): self.assertEqual(NumeroMaximo.NumeroMax(2, 5, 4), ("El valor máximo es 5 y se encuentra en la variable 'y'"))
    def test_TC4(self): self.assertEqual(NumeroMaximo.NumeroMax(4, 1, 5), ("El valor máximo es 5 y se encuentra en la variable 'z'"))
   

# if __name__ == "__main__":
#     unittest.main()