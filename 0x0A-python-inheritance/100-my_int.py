#!/usr/bin/python3
"""This module defines a class MyInt that inherits from int"""


class MyInt(int):
    """A class that inverts int operators == and !="""

    def __eq__(self, value):
        """A class that 0verrides == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """A class that overrides != operator with == behavior"""
        return self.real == value
