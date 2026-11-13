import re
# Ввод функции
def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r'[^\w]', '', text.lower())
    return cleaned == cleaned[::-1]
# Примеры
tests = [
    "А роза упала на лапу Азора",
    "Madam, I'm Adam",
    "Hello, World!",
    "12321",
    "racecar"
]
# Проверка и вывод
for text in tests:
    result = "палиндром" if is_palindrome(text) else "не палиндром"
    print(f"'{text}' — {result}")