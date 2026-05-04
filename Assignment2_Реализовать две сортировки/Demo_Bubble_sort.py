from sorts import bubble_sort

def main():
    original = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", original)
  
    data1 = original.copy()
    bubble_sort(data1)
    print("\nBubble sort (O(n²)):", data1)
    
if __name__ == "__main__":
    main()
