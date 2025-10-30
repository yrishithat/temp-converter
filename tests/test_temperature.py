from converter.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_conversion_roundtrip():
    c = 25
    f = celsius_to_fahrenheit(c)
    assert round(fahrenheit_to_celsius(f), 2) == c
