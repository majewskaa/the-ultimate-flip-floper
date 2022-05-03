from errors import NOTNot1InputError, UndefinedGateError


class Gate:
    def __init__(self):
        pass

    def get_name(self):
        raise UndefinedGateError

    def evaluate(self, values):
        raise UndefinedGateError


class AND(Gate):
    def evaluate(self, values):
        if all(value is True for value in values):
            return True
        else:
            return False

    def get_name(self):
        return 'AND'


class OR(Gate):
    def evaluate(self, values):
        if any(value is True for value in values):
            return True
        else:
            return False

    def get_name(self):
        return 'OR'


class XOR(Gate):        # will output 1 if an odd number of its inputs is 1
    def evaluate(self, values):
        if values.count(True) % 2 == 1:
            return True
        return False

    def get_name(self):
        return 'XOR'


class XNOR(Gate):   # will output 1 if an even number of its inputs is 1
    def evaluate(self, values):
        if values.count(True) % 2 == 0:
            return True
        return False

    def get_name(self):
        return 'XNOR'


class NOR(OR):
    def evaluate(self, values):
        Not = NOT()
        Or = super().evaluate(values)
        return Not.evaluate([Or])

    def get_name(self):
        return 'NOR'


class NAND(AND):
    def evaluate(self, values):
        Not = NOT()
        And = super().evaluate(values)
        return Not.evaluate([And])

    def get_name(self):
        return 'NAND'


class NOT(Gate):
    def evaluate(self, values):
        if type(values) is list:
            if len(values) == 1:
                if values[0] is True:
                    return False
                if values[0] is False:
                    return True
            else:
                raise NOTNot1InputError
        else:
            if values is True:
                return False
            if values is False:
                return True

    def get_name(self):
        return 'NOT'
