from flip_flop import Flip_Flop
from errors import StateValueError
import pytest


def test_flip_flop_simple():
    ff = Flip_Flop(True)
    assert ff.get_value() is True


def test_flip_flop_not_bolean():
    ff = Flip_Flop(1)
    assert ff.get_value() is True
    ff = Flip_Flop(0)
    assert ff.get_value() is False


def test_flip_flop_no_val():
    ff = Flip_Flop()
    assert ff.get_value() is None


def test_flip_flop_val_str():
    ff = Flip_Flop('1')
    assert ff.get_value() is True
    ff = Flip_Flop('0')
    assert ff.get_value() is False


def test_flip_flop_empty_str():
    with pytest.raises(StateValueError):
        Flip_Flop('')


def test_flip_flop_mal1():
    with pytest.raises(StateValueError):
        Flip_Flop(4)


def test_flip_flop_mal2():
    with pytest.raises(StateValueError):
        Flip_Flop('@')
