from flip_flop import Flip_Flop


class Block():
    def __init__(self, gate=None, flip_flop=None):
        if flip_flop is None:
            flip_flop = Flip_Flop()
        self.set_flip_flop(flip_flop)
        self.set_gate(gate)

    def set_flip_flop(self, new_flip_flop):
        self._flip_flop = new_flip_flop

    def set_gate(self, gate):
        self._gate = gate

    def get_flip_flop(self):
        return self._flip_flop

    def get_value(self):
        return self._flip_flop.get_value()

    def get_gate(self):
        return self._gate

    def next_value(self, values):
        next_value = self.get_gate().evaluate(values)
        self.get_flip_flop().set_value(next_value)
