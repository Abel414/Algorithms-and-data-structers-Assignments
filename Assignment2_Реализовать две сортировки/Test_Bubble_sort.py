import unittest
from sorts import bubble_sort, merge_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        cases = [([], []), ([1], [1]), ([2,1], [1,2]), ([3,2,1], [1,2,3])]
        for inp, exp in cases:
            arr = inp[:]
            bubble_sort(arr)
            self.assertEqual(arr, exp)
          
if __name__ == "__main__":
    unittest.main()
