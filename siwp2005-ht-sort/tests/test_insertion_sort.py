import unittest
from sort.insertion_sort import InsertionSort

class TestInsertionSort(unittest.TestCase):

    def test_sort(self):
        data = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        InsertionSort.insertion_sort(data)
        self.assertEqual(data, expected)

if __name__ == '__main__':
    unittest.main()
