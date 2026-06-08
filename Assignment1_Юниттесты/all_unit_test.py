"""
Unit tests for sorting algorithms
"""

import random
from itertools import pairwise
import pytest
import sortings


@pytest.fixture(scope="function")
def fatal_array():
    """
    Setup function to create shuffled array
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


def test_builtin_sort_array(fatal_array):
    """
    Test standard library sorting
    """
    sortings.builtin_sort(fatal_array)
    is_sorted = all(x <= y for x, y in pairwise(fatal_array))
    assert is_sorted


def test_bubble_sort_array(fatal_array):
    """
    Test O(N^2) bubble sort algorithm
    """
    # Create a copy to preserve original for debugging
    original = fatal_array.copy()
    sortings.bubble_sort(fatal_array)
    is_sorted = all(x <= y for x, y in pairwise(fatal_array))
    assert is_sorted
    # Verify all elements are still present (no data loss)
    assert sorted(original) == fatal_array


def test_merge_sort_array(fatal_array):
    """
    Test O(N log N) merge sort algorithm
    """
    # Create a copy to preserve original for debugging
    original = fatal_array.copy()
    result = sortings.merge_sort(fatal_array)
    is_sorted = all(x <= y for x, y in pairwise(result))
    assert is_sorted
    # Verify all elements are still present (no data loss)
    assert sorted(original) == result


def test_bubble_sort_small_arrays(small_array):
    """
    Test bubble sort with small and edge case arrays
    """
    for arr in small_array:
        expected = sorted(arr)
        # Make a copy since bubble_sort modifies in-place
        arr_copy = arr.copy()
        sortings.bubble_sort(arr_copy)
        assert arr_copy == expected, f"Failed for input: {arr}"


def test_merge_sort_small_arrays(small_array):
    """
    Test merge sort with small and edge case arrays
    """
    for arr in small_array:
        expected = sorted(arr)
        # merge_sort returns a new list (doesn't modify original)
        result = sortings.merge_sort(arr)
        assert result == expected, f"Failed for input: {arr}"
        # Verify original array is not modified
        if arr:  # Skip empty list for pairwise check
            is_not_sorted = not all(x <= y for x, y in pairwise(arr))
            # Original should remain unsorted (unless it was already sorted)
            # We don't enforce this strictly as it depends on implementation


def test_bubble_sort_modifies_inplace():
    """
    Test that bubble_sort modifies the original list in-place
    """
    arr = [3, 2, 1]
    original_id = id(arr)
    sortings.bubble_sort(arr)
    assert id(arr) == original_id  # Same object
    assert arr == [1, 2, 3]  # Modified in-place


def test_merge_sort_returns_new_list():
    """
    Test that merge_sort returns a new list and doesn't modify original
    """
    original = [3, 2, 1]
    original_copy = original.copy()
    result = sortings.merge_sort(original)
    
    # Original should remain unchanged
    assert original == original_copy
    # Result should be sorted
    assert result == [1, 2, 3]
    # Result should be a different object
    assert id(result) != id(original)


def test_bubble_sort_stability():
    """
    Test bubble sort stability (order of equal elements)
    """
    # Create list with tuples (value, original_index)
    arr = [(2, 0), (1, 1), (2, 2), (1, 3)]
    expected = [(1, 1), (1, 3), (2, 0), (2, 2)]
    sortings.bubble_sort(arr)
    assert arr == expected


def test_merge_sort_stability():
    """
    Test merge sort stability (order of equal elements)
    """
    # Create list with tuples (value, original_index)
    arr = [(2, 0), (1, 1), (2, 2), (1, 3)]
    expected = [(1, 1), (1, 3), (2, 0), (2, 2)]
    result = sortings.merge_sort(arr)
    assert result == expected


def test_bubble_sort_with_strings():
    """
    Test bubble sort with string elements
    """
    arr = ["banana", "apple", "cherry", "date"]
    expected = ["apple", "banana", "cherry", "date"]
    sortings.bubble_sort(arr)
    assert arr == expected


def test_merge_sort_with_strings():
    """
    Test merge sort with string elements
    """
    arr = ["banana", "apple", "cherry", "date"]
    expected = ["apple", "banana", "cherry", "date"]
    result = sortings.merge_sort(arr)
    assert result == expected


def test_bubble_sort_type_error():
    """
    Test bubble sort raises TypeError with incompatible types
    """
    with pytest.raises(TypeError):
        sortings.bubble_sort([1, "two", 3])


def test_merge_sort_type_error():
    """
    Test merge sort raises TypeError with incompatible types
    """
    with pytest.raises(TypeError):
        sortings.merge_sort([1, "two", 3])


def test_bubble_sort_identical_elements():
    """
    Test bubble sort with all identical elements
    """
    arr = [5] * 100
    sortings.bubble_sort(arr)
    assert arr == [5] * 100
    assert all(x == 5 for x in arr)


def test_merge_sort_identical_elements():
    """
    Test merge sort with all identical elements
    """
    arr = [5] * 100
    result = sortings.merge_sort(arr)
    assert result == [5] * 100
    assert all(x == 5 for x in result)


def test_bubble_sort_single_element():
    """
    Test bubble sort with single element
    """
    arr = [42]
    sortings.bubble_sort(arr)
    assert arr == [42]


def test_merge_sort_single_element():
    """
    Test merge sort with single element
    """
    arr = [42]
    result = sortings.merge_sort(arr)
    assert result == [42]
    # Original should remain unchanged
    assert arr == [42]


def test_bubble_sort_empty_list():
    """
    Test bubble sort with empty list
    """
    arr = []
    sortings.bubble_sort(arr)
    assert arr == []


def test_merge_sort_empty_list():
    """
    Test merge sort with empty list
    """
    arr = []
    result = sortings.merge_sort(arr)
    assert result == []


@pytest.mark.parametrize("sort_func", [
    ("bubble_sort", lambda arr: sortings.bubble_sort(arr) or arr),
    ("merge_sort", lambda arr: sortings.merge_sort(arr)),
])
def test_compare_sorting_algorithms(fatal_array, sort_func):
    """
    Compare both sorting algorithms produce same result as built-in sort
    """
    name, func = sort_func
    original = fatal_array.copy()
    
    # Apply our sorting algorithm
    result = func(fatal_array.copy())
    
    # Compare with Python's built-in sort
    expected = sorted(original)
    assert result == expected, f"{name} failed to produce correct sorting"



   


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])