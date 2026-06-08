import unittest
from sorts import bubble_sort, merge_sort

class TestSorts(unittest.TestCase):
    

    def test_merge_sort(self):
        cases = [([], []), ([1], [1]), ([2,1], [1,2]), ([3,2,1], [1,2,3])]
        for inp, exp in cases:
            self.assertEqual(merge_sort(inp), exp)

if __name__ == "__main__":
    unittest.main()
