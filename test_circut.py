from circut import Circut
from gates import AND, OR, NOT, NOR
from block import Block
from errors import (
    InvalidConnectionError,
    InputIndexError,
    InvalidInputsData,
    NOTNot1InputError,
    StateSizeError,
    StateValueError
)
import pytest


def test_circut_simple():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 3, 2], [0, 1, 2], [2, 1]]
    init_state = '1100'
    circ = Circut(blocks, inputs)
    circ.set_state(init_state)
    assert circ.get_NO_blocks() == 4
    assert circ.get_blocks() == blocks
    assert circ.get_inputs() == inputs
    assert circ.get_state() == [True, True, False, False]
    assert circ.get_inputs_values(3, circ.get_state()) == [False, True]
    circ.next_state()
    assert circ.get_state() == [False, False, False, True]
    assert circ.get_state() == [False, False, False, True]


def test_circut_invalid_connection():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[1, 2], [0, 3, 2], [0, 1, 2], [2, 1]]
    with pytest.raises(InvalidConnectionError):
        Circut(blocks, inputs)


def test_circut_input_index_incorrect():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 7, 2], [0, 1, 2], [2, 1]]
    with pytest.raises(InputIndexError):
        Circut(blocks, inputs)


def test_circut_input_size_incorrect():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[0, 2], [0, 1, 2], [2, 1]]
    with pytest.raises(InvalidInputsData):
        Circut(blocks, inputs)


def test_circut_NOT_more_than_2_inputs():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOT()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 3, 2], [0, 1, 2], [2, 1]]
    with pytest.raises(NOTNot1InputError):
        Circut(blocks, inputs)


def test_circut_no_inputs():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 3, 2], [], [2, 1]]
    with pytest.raises(InvalidConnectionError):
        Circut(blocks, inputs)


def test_circut_incorrect_input_index_type():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 3, 2], ['f', 1, 2], [2, 1]]
    with pytest.raises(InputIndexError):
        Circut(blocks, inputs)


def test_circut_input_index_str_out_range():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 3, 2], ['45', 1, 2], [2, 1]]
    with pytest.raises(InputIndexError):
        Circut(blocks, inputs)


def test_circut_incorrect_state_size():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 3, 2], [0, 1, 2], [2, 1]]
    init_state = '11000'
    circ = Circut(blocks, inputs)
    with pytest.raises(StateSizeError):
        circ.set_state(init_state)


def test_circut_incorrect_state_val():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 3, 2], [0, 1, 2], [2, 1]]
    init_state = '11AA'
    circ = Circut(blocks, inputs)
    with pytest.raises(StateValueError):
        circ.set_state(init_state)
