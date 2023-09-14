from plates import is_valid

def test_length():
    assert is_valid("X") == False
    assert is_valid("XXXXXXX") == False
    assert is_valid("AAA222") == True

def test_start():
    assert is_valid("A2") == False
    assert is_valid("AA") == True
    assert is_valid('11AAA') == False

def test_middle():
    assert is_valid("CS50A") == False
    assert is_valid("CSA50") == True

def test_zero():
    assert is_valid("CS05") == False

def test_ponct():
    assert is_valid("XXX!") == False
