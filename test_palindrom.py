def test_palindrom(input_value, expected):
    input_value = input_value.lower().replace(' ', '')
    return input_value == input_value[::-1]

