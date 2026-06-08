def bubble_sort(data: CompSwapList[Any]) -> None:
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if data.less(j + 1, j):
                data.swap(j, j + 1)
                swapped = True
        if not swapped:
            break
