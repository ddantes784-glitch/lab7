# Ввод функции
def count_words(text: str) -> int:
    return len(text.split())
# Задаем текст
text = input('Введите ваш текст: ')
print(f'Количество слов: {count_words(text)}')