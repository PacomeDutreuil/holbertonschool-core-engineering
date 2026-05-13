#!/usr/bin/env python3
"""Module qui définit la classe Square."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Classe Square qui hérite de Rectangle."""

    def __init__(self, size):
        """Initialise un carré avec une taille donnée."""

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)
