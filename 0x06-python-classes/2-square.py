#!/usr/bin/python3
""" Creating a class square """


class Square:
    """ Defining a class square """
    def __init__(self, size=0):
        """ Initializing a square class
        Args: size=0: size of the square
        """
        if type(size) is not int:
            raise TypeError("sieze must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
