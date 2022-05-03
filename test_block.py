from block import Block
from gates import OR, AND, NOT
from errors import NOTNot1InputError
import pytest


def test_block_simple():
    gate = OR()
    block = Block(gate)
    assert block.get_gate().get_name() == 'OR'
    assert block.get_value() is None
    assert block.get_flip_flop().get_value() is None
    block.get_flip_flop().set_value(False)
    assert block.get_value() is False


def test_block_next_val():
    gate = AND()
    block = Block(gate)
    values = [True, True, True]
    block.next_value(values)
    assert block.get_flip_flop().get_value() is True


def test_block_next_val_NOT_er():
    gate = NOT()
    block = Block(gate)
    values = [True, True, True]
    with pytest.raises(NOTNot1InputError):
        block.next_value(values)
