from numb3rs import validate
import pytest

def test_alpha():
    assert validate("cat") == False
    assert validate("TESTING") == False


def test_range():
    assert validate("64.128.256.512") == False
    assert validate("140.247.235.144") == True