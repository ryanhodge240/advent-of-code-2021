""" Get the data out of the input file """

def parse(data: str):
    """ Get the data out of the input file """
    puzzle_data = []
    for line in data.splitlines():
        coordinates = [x.split(',') for x in line.split()]
        coordinates.pop(1) # Remove the arrow from the list
        # Make each value an integer in the 2D array of coordinates
        puzzle_data.append([[int(y) for y in x] for x in coordinates])
    return puzzle_data
