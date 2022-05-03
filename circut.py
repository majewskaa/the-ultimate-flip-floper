from errors import (
    InvalidConnectionError,
    NOTNot1InputError,
    InvalidInputsData,
    InputIndexError,
    StateSizeError
)


class Circut():
    def __init__(self, blocks, inputs):
        self.set_blocks(blocks)
        self.set_inputs(inputs)
        self.gates_valid()
        self.connection_valid()

    def set_blocks(self, blocks):
        self._blocks = blocks

    def set_state(self, new_state):
        size = self.get_NO_blocks()
        if len(new_state) != size:
            raise StateSizeError(size)
        for value, block in zip(new_state, self.get_blocks()):
            block.get_flip_flop().set_value(value)

    def set_inputs(self, new_inputs):
        size = len(self.get_blocks())
        self._inputs = []
        if type(new_inputs) == list and len(new_inputs) == size:
            for index, inputs in enumerate(new_inputs):
                intputs_list = []
                for one_input in inputs:
                    if type(one_input) == int:
                        pass
                    elif type(one_input) == str and one_input.isdigit():
                        one_input = int(one_input)
                    else:
                        raise InputIndexError(index)
                    if one_input in range(0, size):
                        intputs_list.append(one_input)
                    else:
                        print(f'{one_input}\n{size}')
                        raise InputIndexError(index)
                self._inputs.append(intputs_list)
        else:
            raise InvalidInputsData

    def get_state(self):
        return [block.get_value() for block in self.get_blocks()]

    def get_NO_blocks(self):
        return len(self.get_blocks())

    def get_blocks(self):
        return self._blocks

    def get_inputs(self):
        return self._inputs

    def get_gates(self):
        return [block.get_gate() for block in self.get_blocks()]

    def connection_valid(self):
        end = self.get_NO_blocks() - 1
        inputs_list = self.get_inputs()
        for index, inputs in enumerate(inputs_list):
            if index == 0:
                if end not in inputs:
                    raise InvalidConnectionError(0)
            else:
                input_id = index - 1
                if input_id not in inputs:
                    raise InvalidConnectionError(index)
        return True

    def gates_valid(self):
        for index, gate in enumerate(self.get_gates()):
            no_inputs = len(self.get_inputs()[index])
            if gate.get_name() == 'NOT':
                if no_inputs != 1:
                    raise NOTNot1InputError(index)
            elif gate.get_name() == 'XOR' or gate.get_name() == 'XNOR':
                if no_inputs != 2:
                    msg = f'{gate.get_name()} gate has number of inputs other than 2 at \
flip flop {index}'
                    print(msg)
        return True

    def next_state(self):
        old_state = self.get_state()
        blocks = self.get_blocks()
        for index, block in enumerate(blocks):
            input_val = self.get_inputs_values(index, old_state)
            block.next_value(input_val)

    def get_inputs_values(self, index, old_state):
        inputs = self.get_inputs()[index]
        val_list = [old_state[inputId] for inputId in inputs]
        return val_list
