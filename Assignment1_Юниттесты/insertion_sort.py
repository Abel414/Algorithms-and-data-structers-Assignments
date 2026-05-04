def insertion_sort(data: CompSwapList[Any]) -> None:
    for i in range(1, len(data)):
        j = i
        while j > 0 and data.less(j, j - 1):
            data.swap(j, j - 1)
            j -= 1
