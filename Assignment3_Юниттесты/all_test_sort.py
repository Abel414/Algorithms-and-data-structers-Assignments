import unittest
import random
import string
from sorts import bubble_sort, merge_sort

class TestSortsVicious(unittest.TestCase):

    
    def run_vicious_tests(self, sort_func, inplace=True):
        
        edge_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 5, 5], [5, 5, 5]),
            ([1, 3, 2, 3, 1], [1, 1, 2, 3, 3]), 
        ]
        
        for inp, exp in edge_cases:
            if inplace:
                data = inp[:]  
                sort_func(data)
                self.assertEqual(data, exp)
            else:
                result = sort_func(inp[:])
                self.assertEqual(result, exp)

        
        random.seed(123456)
        big_list = [random.randint(-1000, 1000) for _ in range(1000)]
        if inplace:
            data = big_list[:]
            sort_func(data)
            self.assertEqual(data, sorted(big_list))
        else:
            result = sort_func(big_list[:])
            self.assertEqual(result, sorted(big_list))

        
        reverse_list = list(range(200, 0, -1)) 
        expected = list(range(1, 201))
        if inplace:
            data = reverse_list[:]
            sort_func(data)
            self.assertEqual(data, expected)
        else:
            result = sort_func(reverse_list[:])
            self.assertEqual(result, expected)

        
        already_sorted = list(range(200))
        if inplace:
            data = already_sorted[:]
            sort_func(data)
            self.assertEqual(data, already_sorted)
        else:
            result = sort_func(already_sorted[:])
            self.assertEqual(result, already_sorted)

        
        identical = [42] * 500
        if inplace:
            data = identical[:]
            sort_func(data)
            self.assertEqual(data, identical)
        else:
            result = sort_func(identical[:])
            self.assertEqual(result, identical)

        
        negatives = [-5, -1, -100, -3, -2, -50]
        expected_neg = [-100, -50, -5, -3, -2, -1]
        if inplace:
            data = negatives[:]
            sort_func(data)
            self.assertEqual(data, expected_neg)
        else:
            result = sort_func(negatives[:])
            self.assertEqual(result, expected_neg)

      
        floats = [3.14, 2.71, 1.41, 2.71, 0.5]
        expected_floats = [0.5, 1.41, 2.71, 2.71, 3.14]
        if inplace:
            data = floats[:]
            sort_func(data)
            self.assertEqual(data, expected_floats)
        else:
            result = sort_func(floats[:])
            self.assertEqual(result, expected_floats)

        
        strings = ["banana", "apple", "cherry", "date", "apple"]
        expected_strs = ["apple", "apple", "banana", "cherry", "date"]
        if inplace:
            data = strings[:]
            sort_func(data)
            self.assertEqual(data, expected_strs)
        else:
            result = sort_func(strings[:])
            self.assertEqual(result, expected_strs)

  
        mixed = [0, -3, 5, -1, 0, 2, -4]
        expected_mixed = [-4, -3, -1, 0, 0, 2, 5]
        if inplace:
            data = mixed[:]
            sort_func(data)
            self.assertEqual(data, expected_mixed)
        else:
            result = sort_func(mixed[:])
            self.assertEqual(result, expected_mixed)

        if inplace:
            data = [random.randint(0, 100) for _ in range(50)]
            original_len = len(data)
            sort_func(data)
            self.assertEqual(len(data), original_len)

    
    def test_bubble_sort_vicious(self):
        self.run_vicious_tests(bubble_sort, inplace=True)

    
    def test_merge_sort_vicious(self):
        self.run_vicious_tests(merge_sort, inplace=False)


if __name__ == "__main__":
    unittest.main()
