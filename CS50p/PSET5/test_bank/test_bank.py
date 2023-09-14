from bank import value


def test_lowercase():
    assert value("hello") == 0
    assert value("just a test") == 100
    assert value("hi") == 20

def test_uppercase():
    assert value("OI") == 100
    assert value("HELLO") == 0
    assert value("HOW ARE YOU") == 20

def test_bank():
    assert value("Isso é um teste") == 100
    assert value("How is that") == 20
    assert value("Hello") == 0
