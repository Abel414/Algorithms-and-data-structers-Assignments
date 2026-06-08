"""
Unit tests for sorting algorithms - Vicious edition
"""

import random
from itertools import pairwise
import pytest
import sortings


@pytest.fixture(scope="function")
def fatal_array():
    """
    Setup function to create shuffled array of 1000 elements
    """
    r = random.Random()
    r.seed(123456)

    data = list(range(1000))
    r.shuffle(data)
    yield data


@pytest.fixture(scope="function")
def small_array():
    """
    Setup function for small array edge cases
    """
    return [
        [],  # Empty list
        [1],  # Single element
        [1, 1, 1, 1],  # All equal
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1, 2, 3, 4, 5],  # Already sorted
        [3, 1, 4, 1, 5, 9, 2, 6, 5],  # Random with duplicates
        [-3, -1, -4, -2, 0, 5],  # Negative numbers
    ]


# ========== BUBBLE SORT TESTS (O(n²)) ==========

def test_bubble_sort_array(fatal_array):
    """
    Test O(N^2) bubble sort algorithm on large array
    """
    original = fatal_array.copy()
    sortings.bubble_sort(fatal_array)
    is_sorted = all(x <= y for x, y in pairwise(fatal_array))
    assert is_sorted
    # Verify all elements are still present (no data loss)
    assert sorted(original) == fatal_array


def test_bubble_sort_small_arrays(small_array):
    """
    Test bubble sort with small and edge case arrays
    """
    for arr in small_array:
        expected = sorted(arr)
        arr_copy = arr.copy()
        sortings.bubble_sort(arr_copy)
        assert arr_copy == expected, f"Failed for input: {arr}"


def test_bubble_sort_modifies_inplace():
    """
    Test that bubble_sort modifies the original list in-place
    """
    arr = [3, 2, 1]
    original_id = id(arr)
    sortings.bubble_sort(arr)
    assert id(arr) == original_id
    assert arr == [1, 2, 3]


def test_bubble_sort_stability():
    """
    Test bubble sort stability (order of equal elements preserved)
    """
    arr = [(2, 0), (1, 1), (2, 2), (1, 3)]
    expected = [(1, 1), (1, 3), (2, 0), (2, 2)]
    sortings.bubble_sort(arr)
    assert arr == expected


def test_bubble_sort_with_strings():
    """
    Test bubble sort with string elements
    """
    arr = ["banana", "apple", "cherry", "date"]
    expected = ["apple", "banana", "cherry", "date"]
    sortings.bubble_sort(arr)
    assert arr == expected


def test_bubble_sort_type_error():
    """
    Test bubble sort raises TypeError with incompatible types
    """
    with pytest.raises(TypeError):
        sortings.bubble_sort([1, "two", 3])


def test_bubble_sort_identical_elements():
    """
    Test bubble sort with all identical elements
    """
    arr = [5] * 100
    sortings.bubble_sort(arr)
    assert arr == [5] * 100


def test_bubble_sort_single_element():
    """
    Test bubble sort with single element
    """
    arr = [42]
    sortings.bubble_sort(arr)
    assert arr == [42]


def test_bubble_sort_empty_list():
    """
    Test bubble sort with empty list
    """
    arr = []
    sortings.bubble_sort(arr)
    assert arr == []


def test_bubble_sort_reverse_sorted():
    """
    Test bubble sort with reverse sorted array (worst case)
    """
    arr = list(range(100, 0, -1))
    expected = list(range(1, 101))
    sortings.bubble_sort(arr)
    assert arr == expected


def test_bubble_sort_already_sorted():
    """
    Test bubble sort with already sorted array (best case)
    """
    arr = list(range(100))
    expected = list(range(100))
    sortings.bubble_sort(arr)
    assert arr == expected


# ========== MERGE SORT TESTS (O(n log n)) ==========

def test_merge_sort_array(fatal_array):
    """
    Test O(N log N) merge sort algorithm on large array
    """
    original = fatal_array.copy()
    result = sortings.merge_sort(fatal_array)
    is_sorted = all(x <= y for x, y in pairwise(result))
    assert is_sorted
    assert sorted(original) == result


def test_merge_sort_small_arrays(small_array):
    """
    Test merge sort with small and edge case arrays
    """
    for arr in small_array:
        expected = sorted(arr)
        result = sortings.merge_sort(arr)
        assert result == expected, f"Failed for input: {arr}"


def test_merge_sort_returns_new_list():
    """
    Test that merge_sort returns a new list and doesn't modify original
    """
    original = [3, 2, 1]
    original_copy = original.copy()
    result = sortings.merge_sort(original)
    
    assert original == original_copy
    assert result == [1, 2, 3]
    assert id(result) != id(original)


def test_merge_sort_stability():
    """
    Test merge sort stability (order of equal elements preserved)
    """
    arr = [(2, 0), (1, 1), (2, 2), (1, 3)]
    expected = [(1, 1), (1, 3), (2, 0), (2, 2)]
    result = sortings.merge_sort(arr)
    assert result == expected


def test_merge_sort_with_strings():
    """
    Test merge sort with string elements
    """
    arr = ["banana", "apple", "cherry", "date"]
    expected = ["apple", "banana", "cherry", "date"]
    result = sortings.merge_sort(arr)
    assert result == expected


def test_merge_sort_type_error():
    """
    Test merge sort raises TypeError with incompatible types
    """
    with pytest.raises(TypeError):
        sortings.merge_sort([1, "two", 3])


def test_merge_sort_identical_elements():
    """
    Test merge sort with all identical elements
    """
    arr = [5] * 100
    result = sortings.merge_sort(arr)
    assert result == [5] * 100


def test_merge_sort_single_element():
    """
    Test merge sort with single element
    """
    arr = [42]
    result = sortings.merge_sort(arr)
    assert result == [42]
    assert arr == [42]


def test_merge_sort_empty_list():
    """
    Test merge sort with empty list
    """
    arr = []
    result = sortings.merge_sort(arr)
    assert result == []


def test_merge_sort_reverse_sorted():
    """
    Test merge sort with reverse sorted array
    """
    arr = list(range(100, 0, -1))
    expected = list(range(1, 101))
    result = sortings.merge_sort(arr)
    assert result == expected


def test_merge_sort_already_sorted():
    """
    Test merge sort with already sorted array
    """
    arr = list(range(100))
    expected = list(range(100))
    result = sortings.merge_sort(arr)
    assert result == expected


# ========== COMPARISON TESTS ==========

@pytest.mark.parametrize("sort_func, inplace", [
    ("bubble_sort", True),
    ("merge_sort", False),
])
def test_compare_with_builtin_sort(fatal_array, sort_func, inplace):
    """
    Test both sorting algorithms produce same result as built-in sort
    """
    original = fatal_array.copy()
    expected = sorted(original)
    
    if sort_func == "bubble_sort":
        sort_func_impl = sortings.bubble_sort
        data = original.copy()
        sort_func_impl(data)
        result = data
    else:
        sort_func_impl = sortings.merge_sort
        result = sort_func_impl(original.copy())
    
    assert result == expected, f"{sort_func} failed"


def test_both_sorts_agree_on_random_data():
    """
    Test that bubble sort and merge sort produce the same result
    """
    random.seed(42)
    for _ in range(20):
        size = random.randint(0, 200)
        arr = [random.randint(-100, 100) for _ in range(size)]
        
        bubble_arr = arr.copy()
        sortings.bubble_sort(bubble_arr)
        
        merge_result = sortings.merge_sort(arr)
        
        assert bubble_arr == merge_result, f"Failed for size {size}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])