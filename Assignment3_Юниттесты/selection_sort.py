from sorts import selection_sort

class TestAdditionalSorts(unittest.TestCase):
    def test_selection_sort_vicious(self):
        test_obj = TestSortsVicious()
        test_obj.run_vicious_tests(selection_sort, inplace=True)
