""" Solve part two """

from typing import List

def solve_part_two(puzzle_input: List[List[List[str]]]):
    """ Solve the second part of the question """
    segments = [set() for _ in range(10)]
    segment_dict = {2: 1, 4: 4, 3: 7, 7: 8}
    codes = []
    code = []
    for line in puzzle_input:
        for segment in line[0]:
            number = segment_dict.get(len(segment))
            if number is not None:
                segments[number] = set(segment)
        for segment in line[0]:
            testing_set = set(segment)
            if len(testing_set) == 5 and len(testing_set.intersection(segments[1])) == 2:
                segments[3] = set(segment)
            elif len(testing_set) == 5 and len(testing_set.intersection(segments[4])) == 3:
                segments[5] = set(segment)
            elif len(testing_set) == 5:
                segments[2] = set(segment)

            elif len(testing_set) == 6 and len(testing_set.intersection(segments[4])) == 4:
                segments[9] = set(segment)
            elif len(testing_set) == 6 and len(testing_set.intersection(segments[1])) == 2:
                segments[0] = set(segment)
            elif len(testing_set) == 6:
                segments[6] = set(segment)

        for segment in line[1]:
            current_segment = set(segment)
            for i, num in enumerate(segments):
                if current_segment == num:
                    codes.append(i)
                    break

    count = 0
    summation = 0
    for num in codes:
        code.append(num)
        if count == 3:
            output_sum = [str(x) for x in code]
            summation += int(''.join(output_sum))
            code = []
            count = 0
            continue
        count += 1
    return summation
