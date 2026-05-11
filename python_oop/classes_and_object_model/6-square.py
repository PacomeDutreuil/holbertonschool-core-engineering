#!/usr/bin/env python3
"""Module qui définit une classe Square."""


class Square:
    """Classe représentant un carré."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec une taille et une position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Récupère la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Modifie la position du carré avec validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère #."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))

    def __str__(self):
        """Retourne la représentation du carré."""
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]

        for i in range(self.__size):
            result += (" " * self.__position[0]) + ("#" * self.__size)

            if i != self.__size - 1:
                result += "\n"

        return result
