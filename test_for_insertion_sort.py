import unittest
from comp_swap_container import CompSwapList
import sortings

class TestSorting(unittest.TestCase):
  def test_insertion_sort(self):
        test_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 5, 5], [5, 5, 5]),
        ]
        for inp, exp in test_cases:
            data = CompSwapList(inp)
            sortings.insertion_sort(data)
            self.assertEqual(list(data), exp)
