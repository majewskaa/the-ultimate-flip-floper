from reader import Reader


def test_reader_simple():
    reader = Reader()
    reader.load_from_file('testdata/data1.txt')
    circ = reader.get_data()
    blocks_names = [block.get_gate().get_name() for block in circ.get_blocks()]
    assert blocks_names == ['OR', 'AND', 'NAND', 'OR']
    inputs = [[1, 2, 3], [2, 0], [3, 1], [0, 2]]
    assert circ.get_inputs() == inputs
