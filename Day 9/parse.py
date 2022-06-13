""" Get the data out of the input file """

def parse(data: str):
    """ Get the data out of the input file """
    output_data = data.splitlines()
    output_matrix = [list(line) for line in output_data]
    return [[int(num) for num in line] for line in output_matrix] 
