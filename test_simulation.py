from simulation import Simulation
from circut import Circut
from block import Block
from gates import AND, OR, NOR, NAND
from errors import InvalidNOStepsError
import pytest


def test_simulation_simple_data():
    gate1 = OR()
    gate2 = AND()
    gate3 = NOR()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[3, 2], [0, 3, 2], [0, 1, 2], [2, 1]]
    init_state = '1100'
    NO_steps = 7
    loop = False
    sim = Simulation()
    sim.set_NO_steps(NO_steps)
    circut = Circut(blocks, inputs)
    sim.set_circut(circut)
    circut.set_state(init_state)
    sim._states = []
    sim.add_state(circut.get_state())
    sim._loop = loop
    assert sim.get_NO_steps() == 7
    assert sim.get_circut().get_NO_blocks() == 4
    assert sim.str_state(sim.get_states()[0]) == '1100'
    assert sim._loop is False


def test_simulation_function():
    gate1 = OR()
    gate2 = AND()
    gate3 = NAND()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[1, 2, 3], [0, 2], [3, 1], [0, 2]]
    init_state = '1100'
    NO_steps = 6
    loop = False
    sim = Simulation()
    sim.set_NO_steps(NO_steps)
    circut = Circut(blocks, inputs)
    sim.set_circut(circut)
    circut.set_state(init_state)
    sim._states = []
    sim.add_state(sim.str_state(circut.get_state()))
    sim._loop = loop
    sim.simulation()
    list_of_states = sim.get_states()
    assert list_of_states[0] == '1100'
    assert list_of_states[1] == '1011'
    assert list_of_states[2] == '1111'
    assert list_of_states[3] == '1101'
    assert list_of_states[4] == '1001'
    assert list_of_states[5] == '1011'
    assert list_of_states[6] == '1111'
    msg = 'Generated 5 combinations out of 16 possible combinations.'
    assert sim.str_space_usage() == msg
    assert sim.str_bits_diversity() == 'States differ on average by 1.43 bits.'


def test_simulation_function_loop():
    gate1 = OR()
    gate2 = AND()
    gate3 = NAND()
    gate4 = OR()
    blocks = [Block(gate1), Block(gate2), Block(gate3), Block(gate4)]
    inputs = [[1, 2, 3], [0, 2], [3, 1], [0, 2]]
    init_state = '1100'
    loop = True
    sim = Simulation()
    circut = Circut(blocks, inputs)
    sim.set_circut(circut)
    circut.set_state(init_state)
    sim._states = []
    sim.add_state(sim.str_state(circut.get_state()))
    sim._loop = loop
    sim.simulation()
    list_of_states = sim.get_states()
    assert sim._loop is True
    assert list_of_states[0] == '1100'
    assert list_of_states[1] == '1011'
    assert list_of_states[2] == '1111'
    assert list_of_states[3] == '1101'
    assert list_of_states[4] == '1001'
    msg = 'Generated 5 combinations out of 16 possible combinations.'
    assert sim.str_space_usage() == msg
    assert sim.str_bits_diversity() == 'States differ on average by 1.6 bits.'


def test_simulation_NO_steps():
    sim = Simulation()
    with pytest.raises(InvalidNOStepsError):
        sim.set_NO_steps('g')
