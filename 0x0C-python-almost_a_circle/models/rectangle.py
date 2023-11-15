#!/usr/bin/python3
""" Module that contains class Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        self.set_dimensions(width, height)
        self.set_position(x, y)
        super().__init__(id)

    def set_dimensions(self, width, height):
        """ Set dimensions """
        self.__width = self.validate_positive_integer("width", width)
        self.__height = self.validate_positive_integer("height", height)

    def set_position(self, x, y):
        """ Set position """
        self.__x = self.validate_non_negative_integer("x", x)
        self.__y = self.validate_non_negative_integer("y", y)

    @staticmethod
    def validate_positive_integer(attr_name, value):
        """ Validate positive integer """
        if type(value) is not int:
            raise TypeError(f"{attr_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")
        return value

    @staticmethod
    def validate_non_negative_integer(attr_name, value):
        """ Validate non-negative integer """
        if type(value) is not int:
            raise TypeError(f"{attr_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")
        return value

    def area(self):
        """ returns the area of the rectangle object """
        return self.__width * self.__height

    def display(self):
        """ displays a rectangle """
        rectangle = self.__y * "\n"
        for _ in range(self.__height):
            rectangle += (" " * self.__x)
            rectangle += ("#" * self.__width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str special method """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ update method """
        if args:
            self.set_dimensions(args[1] if len(args) > 1 else self.__width,
                                args[2] if len(args) > 2 else self.__height)
            self.set_position(args[3] if len(args) > 3 else self.__x,
                              args[4] if len(args) > 4 else self.__y)
        else:
            if 'width' in kwargs or 'height' in kwargs:
                new_width = kwargs.get('width', self.__width)
                new_height = kwargs.get('height', self.__height)
                self.set_dimensions(new_width, new_height)
            if 'x' in kwargs or 'y' in kwargs:
                new_x = kwargs.get('x', self.__x)
                new_y = kwargs.get('y', self.__y)
                self.set_position(new_x, new_y)


    def to_dictionary(self):
        """ method that returs a dictionary with properties """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
        }
