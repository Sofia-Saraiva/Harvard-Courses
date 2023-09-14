import pytest
from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"

def test_valueerror():
     with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")

def test_wominutes():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_outrange():
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")

def test_to():
    with pytest.raises(ValueError):
        convert(" to ")
