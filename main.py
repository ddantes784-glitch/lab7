def vigenere_cipher(text: str, key: str, decrypt: bool = False) -> str:
    result = []
    key = key.lower()
    key_index = 0
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            
            if decrypt:
                shift = -shift
                
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
            key_index += 1
        else:
            result.append(char)
            
    return "".join(result)

original_text = "Hello, World!"
secret_key = "key"

encrypted_text = vigenere_cipher(original_text, secret_key)
print(f"Оригинал:    {original_text}")
print(f"Зашифровано: {encrypted_text}")

decrypted_text = vigenere_cipher(encrypted_text, secret_key, decrypt=True)
print(f"Расшифровано:{decrypted_text}")