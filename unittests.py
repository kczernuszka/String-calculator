from hello import read_numbers_from_string, add
import unittest

class Test_TestAddition(unittest.TestCase):

    def test_read_numbers_from_empty_string(self):
        self.assertFalse(read_numbers_from_string(""))

    def test_read_numbers_from_string(self):
        self.assertEqual(read_numbers_from_string("1"), [1])
        self.assertEqual(read_numbers_from_string("1,2,3"), [1,2,3])
    
    def test_add_numbers(self):
        self.assertEqual(add(""), 0)
        self.assertEqual(add("4,5,2,7"), 18)

if __name__ == '__main__':
    unittest.main()       
    