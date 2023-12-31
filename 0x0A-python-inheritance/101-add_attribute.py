#!/usr/bin/python3
"""Module for the add_attribute function."""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if it's possible."""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")


if __name__ == "__main__":
    add_attribute = __import__('101-add_attribute').add_attribute

    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
