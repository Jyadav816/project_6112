import unittest

class TestSum(unittest.TestCase):
    def test_list_int(self):
        # Test to find the min value in the list
        data_value = [7, 5, 8]
        result = min(data_value)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()