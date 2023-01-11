#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """A class that represents a student."""

    def __init__(self, first_name, last_name, age):
        """A class that initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A class that gets a dictionary
        representation of the Student"""
        return self.__dict__
