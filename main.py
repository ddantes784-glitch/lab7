def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)
# Шифрование
original = "Hello, World!"
encrypted = caesar_cipher(original, 3)
print(f"Оригинал: {original}")
print(f"Зашифровано: {encrypted}")
# Расшифровка
decrypted = caesar_cipher(encrypted, -3)
print(f"Расшифровано: {decrypted}")