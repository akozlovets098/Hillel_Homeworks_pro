from typing import Generator


def generate_range(start, end, step=1) -> Generator:
    '''
    function that creates the generator analogical to function range
    :param start: starting number (included to range)
    :param end: ending number (excluded from range)
    :param step: difference between numbers in range that are next to each other
    :return: range generator
    '''
    numb = start
    while numb < end:
        yield numb
        numb += step


print(generate_range(1, 11, 2))
print(list(generate_range(1, 11, 2)))