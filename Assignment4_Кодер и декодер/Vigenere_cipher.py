def vigenere_encode(text, key):
    result = []
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            key_char = key[key_index % key_length]
            shift = ord(key_char.lower()) - ord('a')
            
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)


def vigenere_decode(text, key):
    result = []
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            key_char = key[key_index % key_length]
            shift = ord(key_char.lower()) - ord('a')
            
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)


