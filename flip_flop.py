from errors import StateValueError


class Flip_Flop():
    def __init__(self, value=None):
        self.set_value(value)

    def set_value(self, new_value):
        if type(new_value) == bool or new_value is None:
            self._value = new_value
        elif new_value in [1, '1']:
            self._value = True
        elif new_value in [0, '0']:
            self._value = False
        else:
            raise StateValueError

    def get_value(self):
        return self._value
