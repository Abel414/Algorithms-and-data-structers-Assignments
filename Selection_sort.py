def selection_sort(data: CompSwapList[Any]) -> None:
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data.less(j, min_idx):
                min_idx = j
        if min_idx != i:
            data.swap(i, min_idx)
