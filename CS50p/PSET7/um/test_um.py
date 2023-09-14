import pytest
from um import count


def test_upper():
    assert count("Um, thanks, Um") == 2

def test_space():
    assert count("Um,  UM   , um") == 3

def test_words():
    assert count("Um? Mum? album um, umm, clumsy alums drums?") == 2