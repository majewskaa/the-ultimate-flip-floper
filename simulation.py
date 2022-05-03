from itertools import combinations
from interface import Interface
from errors import InvalidNOStepsError


class Simulation():
    def __init__(self):
        pass

    def set_NO_steps(self, NO_steps):
        if type(NO_steps) == int:
            self._number_of_steps = NO_steps
        elif type(NO_steps) == str and NO_steps.isdigit():
            self._number_of_steps = int(NO_steps)
        else:
            raise InvalidNOStepsError

    def set_circut(self, circut):
        self._circut = circut

    def set_loop(self, loop):
        self._loop = loop

    def add_state(self, new_state):
        self._states.append(new_state)

    def get_NO_steps(self):
        return self._number_of_steps

    def get_circut(self):
        return self._circut

    def get_states(self):
        return self._states

    def process(self):
        interface = Interface()
        interface.start()
        circut = interface.get_circut()
        interface.set_user_data(self)
        self._states = []
        self.add_state(self.str_state(circut.get_state()))
        self.set_circut(circut)
        self.simulation()
        interface.write_outputfile(self)

    def simulation(self):
        if self._loop is False:
            self.iteration()
        else:
            self.iteration_loop()

    def iteration(self):
        circ = self.get_circut()
        for _ in range(0, self.get_NO_steps()):
            circ.next_state()
            state = self.str_state(circ.get_state())
            self.add_state(state)

    def iteration_loop(self):
        circ = self.get_circut()
        state = None
        while state not in self.get_states():
            if state is not None:
                self.add_state(state)
            circ.next_state()
            state = self.str_state(circ.get_state())

    def str_space_usage(self):
        states = self.get_states()
        NO_combinations = len(set(states))
        NO_FF = self.get_circut().get_NO_blocks()
        NO_possible_comb = pow(2, NO_FF)
        msg = f'Generated {NO_combinations} combinations out of {NO_possible_comb} \
possible combinations.'
        return msg

    def str_bits_diversity(self):
        states = self.get_states()
        diff_count = 0
        comb = list(combinations(states, 2))
        for (state1, state2) in comb:
            for val1, val2 in zip(state1, state2):
                if val1 != val2:
                    diff_count += 1
        NO_comb = len(comb)
        average = round(diff_count / NO_comb, 2)
        msg = f'States differ on average by {average} bits.'
        return msg

    def str_state(self, state):
        str_state = ''
        for value in state:
            str_state += str(int(value))
        return str_state
