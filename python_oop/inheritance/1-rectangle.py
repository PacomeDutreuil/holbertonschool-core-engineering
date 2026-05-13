#!/usr/bin/env python3
"""Module qui définit la classe Rectangle."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Rectangle qui hérite de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise un rectangle avec width et height."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
