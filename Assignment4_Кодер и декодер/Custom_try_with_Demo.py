
def encode(text, key):
    result = []
    for i, char in enumerate(text):
        key_char = ord(key[i % len(key)])
        encoded_ord = ord(char) ^ key_char
        result.append(format(encoded_ord, '02x'))
    return ''.join(result)


def decode(encoded, key):
    result = []
    hex_pairs = [encoded[i:i+2] for i in range(0, len(encoded), 2)]
    
    for i, hex_pair in enumerate(hex_pairs):
        key_char = ord(key[i % len(key)])
        decoded_ord = int(hex_pair, 16) ^ key_char
        result.append(chr(decoded_ord))
    return ''.join(result)


# Demo
if __name__ == "__main__":
    original = "Hello, World! This is my secret message."
    key = "secretkey123"
    
    encoded = encode(original, key)
    decoded = decode(encoded, key)
    
    print(f"Original: {original}")
    print(f"Key:      {key}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {decoded}")
