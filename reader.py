from gates import AND, OR, XOR, XNOR, NOR, NAND, NOT
from block import Block
from circut import Circut
from errors import (
    DataFormatError,
    GateNameError
)


class Reader():
    def __init__(self):
        pass

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def load_from_file(self, file_handle):
        path = file_handle
        with open(path) as file_handle:
            self.set_data(self.read_circut_from_file(file_handle))

    def read_circut_from_file(self, file_handle):
        blocks = []
        inputs = []
        for line in file_handle:
            line = line.rstrip('\n')
            line = line.strip()
            line = line.split(',')
            if len(line) == 2:
                gate_name = line[0]
                gate = self.create_gate(gate_name)
                block = Block(gate)
                inputs.append(line[1].split(';'))
                blocks.append(block)
            else:
                raise DataFormatError
        circut = Circut(blocks, inputs)
        return circut

    def create_gate(self, gate_name):
        gates_names = ['AND', 'OR', 'XOR', 'XNOR', 'NOR', 'NAND', 'NOT']
        if type(gate_name) == str:
            if gate_name in gates_names:
                if gate_name == 'AND':
                    gate = AND()
                elif gate_name == 'OR':
                    gate = OR()
                elif gate_name == 'NOT':
                    gate = NOT()
                elif gate_name == 'NAND':
                    gate = NAND()
                elif gate_name == 'NOR':
                    gate = NOR()
                elif gate_name == 'XOR':
                    gate = XOR()
                elif gate_name == 'XNOR':
                    gate = XNOR()
                return gate
            else:
                raise GateNameError(gate_name)
        else:
            raise GateNameError
