from comp_swap_container import CompSwapList

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if data.less(j + 1, j):
                data.swap(j, j + 1)
                swapped = True
        if not swapped:
            break

def insertion_sort(data):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data.less(j, j - 1):
            data.swap(j, j - 1)
            j -= 1

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data.less(j, min_idx):
                min_idx = j
        if min_idx != i:
            data.swap(i, min_idx)