class InvalidInputsData(Exception):
    def __init__(self):
        super().__init__('Inputs data format incorrect')


class NOTNot1InputError(Exception):
    def __init__(self, id=''):
        msg = f'NOT has number of inputs other than 1 at flip flop {id}'
        super().__init__(msg)


class DataFormatError(Exception):
    def __init__(self, id=''):
        msg = 'Invalid data format'
        super().__init__(msg)


class StateValueError(Exception):
    def __init__(self):
        msg = 'States values should be 0 or 1'
        super().__init__(msg)


class InvalidConnectionError(Exception):
    def __init__(self, id=''):
        msg = f'Flip flop {id} is not connected to the one before it'
        super().__init__(msg)


class GateNameError(Exception):
    def __init__(self, gate_name=''):
        super().__init__(f'Invalid gate {gate_name}. Possible gates are: \
AND, OR, XOR, XNOR, NOR, NAND, NOT')


class InputIndexError(Exception):
    def __init__(self, id=''):
        super().__init__(f'Input index incorrect at block {id}')


class InvalidNOStepsError(Exception):
    def __init__(self):
        super().__init__('Number Of steps should be digit')


class UndefinedGateError(Exception):
    def __init__(self):
        super().__init__("Gate is undefined")


class StateSizeError(Exception):
    def __init__(self, size):
        super().__init__(f'State should have {size} values')
