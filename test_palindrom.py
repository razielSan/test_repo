def test_palindrom(input_value: str, expected: str):
    """
        Вычисляет явлеяется ли строка полиндромом
    """
    input_value = input_value.lower().replace(' ', '')
    return input_value == input_value[::-1]
