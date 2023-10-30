#!/usr/bin/python3
"""
This module contains the function say_my_name which prints a name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a name in the format "My name is <first name> <last name>".
    
    Args:
        first_name: First name, must be a string.
        last_name: Last name (default is an empty string), must be a string.
    
    Raises:
        TypeError: If first_name or last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
