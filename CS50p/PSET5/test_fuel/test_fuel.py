from fuel import convert, gauge
import pytest

def test_fraction():
    assert convert("3/4") == 75 and gauge(75) == "75%"

def test_f():
    assert gauge(100) == "F" and convert("4/4") == 100
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_e():
    assert gauge(0) == "E" and convert("0/4") == 0
    assert convert("1/100") == 1 and gauge(1) == "E"

def test_error():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")