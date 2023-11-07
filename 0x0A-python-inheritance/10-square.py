#!/usr/bin/python3
"""Module for the Square class."""


class BaseGeometry:
    """A class with public instance method area."""
    def area(self):
        """Method not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as an integer greater than 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry class."""
    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """A class that inherits from Rectangle class."""
    def __init__(self, size):
        """Initialize a Square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] {self.__size}/{self.__size}"
