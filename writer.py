class Writer:
    def __init__(self):
        pass

    def write_output_file(self, filepath, simulation):
        path = filepath
        handle = open(path, 'w')
        data = simulation.get_states()
        for state in data:
            handle.write(f'{state}\n')
        handle.write(f'{simulation.str_space_usage()}\n\
{simulation.str_bits_diversity()}')
