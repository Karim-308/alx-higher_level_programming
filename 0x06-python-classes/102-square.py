#!/usr/bin/python3
class Square:
    """Represents a Square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (float or int): Size of the side of the Square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have the same area, False otherwise."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if squares have different areas, False otherwise."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if the current square has a smaller area than the other, False otherwise."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if the current square has a smaller or equal area than the other, False otherwise."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if the current square has a bigger area than the other, False otherwise."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if the current square has a bigger or equal area than the other, False otherwise."""
        return self.area() >= other.area()
