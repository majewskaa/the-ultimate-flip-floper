from gates import AND, OR, XOR, XNOR, NOT, NOR, NAND, Gate
from errors import NOTNot1InputError, UndefinedGateError
import pytest


def test_AND_1():
    states = [True, True, True, True]
    gate = AND()
    assert gate.evaluate(states) is True


def test_AND_0():
    states = [True, False, True, True]
    gate = AND()
    assert gate.evaluate(states) is False


def test_AND_only_1():
    states = [True]
    gate = AND()
    assert gate.evaluate(states) is True


def test_AND_only_0():
    states = [False]
    gate = AND()
    assert gate.evaluate(states) is False


def test_OR_1():
    states = [True, False, False, True]
    gate = OR()
    assert gate.evaluate(states) is True


def test_OR_0():
    states = [False, False, False, False]
    gate = OR()
    assert gate.evaluate(states) is False


def test_OR_only_1():
    states = [True]
    gate = OR()
    assert gate.evaluate(states) is True


def test_OR_only_0():
    states = [False]
    gate = OR()
    assert gate.evaluate(states) is False


def test_XOR_1():
    states = [True, False]
    gate = XOR()
    assert gate.evaluate(states) is True


def test_XOR_0():
    states = [True, True]
    gate = XOR()
    assert gate.evaluate(states) is False


def test_XOR_three_inputs_1():
    states = [True, True, True]
    gate = XOR()
    assert gate.evaluate(states) is True


def test_XOR_three_inputs_0():
    states = [False, False, False]
    gate = XOR()
    assert gate.evaluate(states) is False


def test_XNOR_all_1():
    states = [True, True]
    gate = XNOR()
    assert gate.evaluate(states) is True


def test_XNOR_all_0():
    states = [False, False]
    gate = XNOR()
    assert gate.evaluate(states) is True


def test_XNOR_three_inputs_1():
    states = [True, True, True]
    gate = XNOR()
    assert gate.evaluate(states) is False


def test_XNOR_three_inputs_0():
    states = [False, True, False]
    gate = XNOR()
    assert gate.evaluate(states) is False


def test_NOT_1():
    states = [False]
    gate = NOT()
    assert gate.evaluate(states) is True


def test_NOR_1():
    states = [True, False, False, True]
    gate = NOR()
    assert gate.evaluate(states) is False


def test_NOR_0():
    states = [False, False, False, False]
    gate = NOR()
    assert gate.evaluate(states) is True


def test_NOR_only_1():
    states = [True]
    gate = NOR()
    assert gate.evaluate(states) is False


def test_NOR_only_0():
    states = [False]
    gate = NOR()
    assert gate.evaluate(states) is True


def test_NAND_1():
    states = [True, True, True, True]
    gate = NAND()
    assert gate.evaluate(states) is False


def test_NAND_0():
    states = [True, False, True, True]
    gate = NAND()
    assert gate.evaluate(states) is True


def test_NAND_only_1():
    states = [True]
    gate = NAND()
    assert gate.evaluate(states) is False


def test_NAND_only_0():
    states = [False]
    gate = NAND()
    assert gate.evaluate(states) is True


def test_get_name():
    gate = NAND()
    assert gate.get_name() == 'NAND'


def test_NOT_no_1_input():
    gate = NOT()
    with pytest.raises(NOTNot1InputError):
        gate.evaluate([True, True])


def test_indef_gate():
    gate = Gate()
    with pytest.raises(UndefinedGateError):
        gate.evaluate([True, True])
