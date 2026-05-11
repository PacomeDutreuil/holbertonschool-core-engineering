#!/usr/bin/env python3
"""Module qui définit une classe Square."""


class Square:
    """Classe représentant un carré."""

    def __init__(self, size=0):
        """Initialise un carré avec une taille."""
        self.size = size

    @property
    def size(self):
        """Récupère la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère #."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
