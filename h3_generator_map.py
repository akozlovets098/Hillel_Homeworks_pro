from typing import Callable, List, Generator


def generate_map(some_function: Callable, list_of_items: List) -> Generator:
    '''
    function which executes parameter function on each item in parameter list of items and creates generator of
    the resulting items
    :param some_function: function to be executed
    :param list_of_items: list of items on which the function is to be executed
    :return: generator of resulting items
    '''
    for item in list_of_items:
        yield some_function(item)


print(generate_map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(list(generate_map(lambda x: x**2, [1, 2, 3, 4, 5])))