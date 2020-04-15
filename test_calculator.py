from calculator import Calculator
import unittest

class Test_TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
    
    def test_validate_tokens(self):
        self.assertRaises(Exception, self.calculator.add, "wrongString")
        self.assertRaises(Exception, self.calculator.add, "1,2,g,3,7,8")
        self.assertRaises(Exception, self.calculator.add, "1,\n2,3,3,7,8")
        self.assertRaises(Exception, self.calculator.add, "\\;\n1,2,3")

    def test_calculation_from_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)
        self.assertEqual(self.calculator.multiply(""), 0)

    def test_calculation_from_string(self):
        self.assertEqual(self.calculator.add("3,9,15"), 27)
        self.assertEqual(self.calculator.multiply("3,9,15"), 405)

    def test_calculation_from_string_with_new_lines(self):
        self.assertEqual(self.calculator.add("3\n9\n15"), 27)
        self.assertEqual(self.calculator.add("3\n9,15"), 27)

    def test_calculation_from__string_with_negative_numbers(self):
        self.assertEqual(self.calculator.add("3,-9,15"), 9)

    def test_calculation_from_string_with_changing_delimiter(self):
        self.assertEqual(self.calculator.add("\\;\n3;9;15"), 27)
        self.assertEqual(self.calculator.add("\\;\n3;9\n15"), 27)
        self.assertEqual(self.calculator.add("\\;\n3\n9\n15"), 27)

    def test_calculation_from_string_with_multiple_delimiters(self):
        self.assertEqual(self.calculator.add("\\[;,@]\n3;9,15@45"), 72)

if __name__ == '__main__':
    unittest.main()       
    