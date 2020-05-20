# Unit testing Program Script

from typing import Union

def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError('The divisor can\'t be Zero')
        
    return dividend / divisor


def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError('Pass at least one value')

    total = 1
    for arg in args:
        total *= arg
        
    return total


