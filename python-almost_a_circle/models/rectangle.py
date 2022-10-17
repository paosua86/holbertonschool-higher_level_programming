#!/usr/bin/python3
"""
Contains rectangle
"""
from models.base import Base


class Rectangle(Base):
    """representation of a rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """set width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """set x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """set y"""
        self.__y = value
