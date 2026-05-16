
def caesar_encode(text, shift):
    
    result = []
    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)





def caesar_decode(text, shift):
    
    return caesar_encode(text, -shift)

def brute_force_caesar(encoded_text):
   
    results = []
    for shift in range(1, 26):
        decoded = caesar_encode(encoded_text, -shift)
        results.append((shift, decoded))
    return results


