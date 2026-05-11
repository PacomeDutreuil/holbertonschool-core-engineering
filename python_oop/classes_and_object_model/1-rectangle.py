#!/usr/bin/env python3
"""Module qui définit une classe Rectangle."""


class Rectangle:
    """Classe représentant un rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec une largeur et une hauteur."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Modifie la largeur avec validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifie la hauteur avec validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
