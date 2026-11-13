import json

def is_valid_json(json_string: str) -> bool:
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False
tests = [
    '{"name": "Иван", "age": 25}',
    '[1, 2, 3, "test"]',
    '{"name": "Иван", "age": 25,}',
    '{name: "Иван", "age": 25}',
    'Просто строка',
    '{"key": "value"'
]
for i, test_str in enumerate(tests, 1):
    result = "Валидный" if is_valid_json(test_str) else "Невалидный"
    print(f"Тест {i}: {result:<12} | {test_str}")