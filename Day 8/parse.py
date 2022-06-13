""" Get the data out of the input file """

def parse(data: str):
    """ Get the data out of the input file """
    output_list = []
    for line in data.splitlines():
        output_list.append([x.split() for x in line.split('|')])
    return output_list
