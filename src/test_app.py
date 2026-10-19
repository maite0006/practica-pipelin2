from app import saludo


def test_saludo():
    assert saludo("Ana") == "Hola, Ana!"
