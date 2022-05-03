from errors import InvalidNOStepsError
from reader import Reader
from writer import Writer
import sys
from errors import (
    DataFormatError,
    GateNameError,
    InvalidConnectionError,
    NOTNot1InputError,
    InvalidInputsData,
    InputIndexError,
    StateValueError,
    StateSizeError
)


class Interface:
    def __init__(self):
        pass

    def start(self):
        print("Write 'exit' anytime to end.")

    def set_user_data(self, sim):
        loop = self.till_loop()
        sim.set_loop(loop)
        if loop is False:
            self.set_NO_steps(sim)

    def set_initial_state(self, circut):
        initial_state = None
        while not initial_state:
            initial_state = input('Initial state: ')
            if initial_state == 'exit':
                sys.exit()
            try:
                circut.set_state(initial_state)
            except StateValueError as m:
                print(m)
                initial_state = None
            except StateSizeError as m:
                print(m)
                initial_state = None

    def set_NO_steps(self, sim):
        no_steps = None
        while not no_steps:
            no_steps = input('Number of steps: ')
            if no_steps == 'exit':
                sys.exit()
            try:
                sim.set_NO_steps(no_steps)
            except InvalidNOStepsError as m:
                print(m)
                no_steps = None

    def get_circut(self):
        reader = Reader()
        inputfile = None
        while not inputfile:
            inputfile = input('Input file path: ')
            if inputfile == 'exit':
                sys.exit()
            try:
                reader.load_from_file(inputfile)
            except FileNotFoundError:
                print('Could not find circut database')
                inputfile = None
            except PermissionError:
                print("You don't have permission to open circut database")
                inputfile = None
            except IsADirectoryError:
                print('Database should be file, not directory')
                inputfile = None
            except GateNameError as m:
                print(m)
                inputfile = None
            except DataFormatError as m:
                print(m)
                inputfile = None
            except InvalidConnectionError as m:
                print(m)
                inputfile = None
            except NOTNot1InputError as m:
                print(m)
                inputfile = None
            except InvalidInputsData as m:
                print(m)
                inputfile = None
            except InputIndexError as m:
                print(m)
                inputfile = None
        circut = reader.get_data()
        self.set_size(circut.get_NO_blocks())
        self.set_initial_state(circut)
        return circut

    def write_outputfile(self, simulaion):
        writer = Writer()
        outputfile = None
        while not outputfile:
            outputfile = input('Output file: ')
            if outputfile == 'exit':
                sys.exit()
            try:
                writer.write_output_file(outputfile, simulaion)
            except PermissionError:
                print("You don't have permission to overwrite this file")
                outputfile = None
            except IsADirectoryError:
                print('This is already a directory name')
                outputfile = None
        return outputfile

    def set_size(self, size):
        self._size = size

    def till_loop(self):
        loop = input('Should program stop at loop?\n1. yes\t2. no\n')
        while loop not in ['1', '2']:
            if loop == 'exit':
                sys.exit()
            loop = input("Type '1' for 'yes' or '2' for 'no'!\n")
        if loop == '1':
            return True
        else:
            return False
