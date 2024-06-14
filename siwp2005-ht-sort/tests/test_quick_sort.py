import unittest
from sort.quick_sort import QuickSort

class TestQuickSort(unittest.TestCase):

    def test_sort(self):
        data = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        sorted_data = QuickSort.quick_sort(data)
        self.assertEqual(sorted_data, expected)

if __name__ == '__main__':
    unittest.main()
