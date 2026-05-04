rom sorts import bubble_sort, merge_sort

def main():
  
    original = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", original)
  
    data2 = original.copy()
    sorted_data = merge_sort(data2)
    print("Merge sort (O(n log n)):", sorted_data)
  
if __name__ == "__main__":
    main()
