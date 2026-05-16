# Demo
if __name__ == "__main__":
    original = "Hello, World! This is a secret message."
    key = "KEY"
    
    encoded = vigenere_encode(original, key)
    decoded = vigenere_decode(encoded, key)
    
    print(f"Original: {original}")
    print(f"Key:      {key}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {decoded}")
