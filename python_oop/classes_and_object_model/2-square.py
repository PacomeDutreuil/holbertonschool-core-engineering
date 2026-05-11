#!/usr/bin/env python3
"""Module qui définit une classe Square."""


class Square:
    """Classe représentant un carré."""

    def __init__(self, size=0):
        """Initialise un carré avec validation de la taille."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
