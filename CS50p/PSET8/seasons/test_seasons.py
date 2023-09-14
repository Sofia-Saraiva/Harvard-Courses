import pytest
from seasons import convert


def test_seasons():
    assert convert("2021-11-29") == "Five hundred twenty-five thousand, six hundred minutes"

