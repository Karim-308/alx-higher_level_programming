#!/usr/bin/python3
"""
This module contains the function add_integer which adds two numbers.
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b.
    
    Args:
        a: The first parameter, must be an integer or a float.
        b: The second parameter (default is 98), must be an integer or a float.
    
    Returns:
        The sum of a and b casted to an integer.
    
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
