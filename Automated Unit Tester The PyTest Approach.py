import unittest

# The function we want to test
def add_numbers(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(add_numbers(10, 5), 15)
        self.assertEqual(add_numbers(-1, 1), 0)
        
    def test_strings(self):
        # Testing if it handles strings correctly
        self.assertEqual(add_numbers("GitHub", "Code"), "GitHubCode")

if __name__ == '__main__':
    unittest.main()