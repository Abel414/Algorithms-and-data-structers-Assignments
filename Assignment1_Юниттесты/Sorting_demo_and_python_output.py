from comp_swap_container import CompSwapList
import sortings

data = CompSwapList([3, 1, 4, 1, 5, 9, 2])
print("Before:", list(data))
sortings.bubble_sort(data)  
print("After: ", list(data))
print(f"Comparisons: {data.comps}, Swaps: {data.swaps}")

#My python output

...
----------------------------------------------------------------------
Ran 3 tests in 0.012s

OK
