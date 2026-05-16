from sorts import insertion_sort

class TestAdditionalSorts(unittest.TestCase):
    def test_insertion_sort_vicious(self):
        test_obj = TestSortsVicious()
        test_obj.run_vicious_tests(insertion_sort, inplace=True)
    
  
