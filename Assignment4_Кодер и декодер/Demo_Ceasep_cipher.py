if __name__ == "__main__":
    original = "Hello, World!"
    shift = 3
    
    encoded = caesar_encode(original, shift)
    decoded = caesar_decode(encoded, shift)
    
    print(f"Original: {original}")
    print(f"Encoded (shift {shift}): {encoded}")
    print(f"Decoded: {decoded}")
    
    print("\n force all shifts ")
    for shift_attempt, result in brute_force_caesar(encoded):
        print(f"Shift {shift_attempt:2}: {result}")
