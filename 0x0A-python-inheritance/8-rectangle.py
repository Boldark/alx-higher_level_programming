#!/usr/bin/python3
"""Module inheris from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """A class that ntializes a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
