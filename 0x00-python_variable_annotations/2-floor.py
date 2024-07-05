#!/usr/bin/env python3

""" Type-annotated function floor which takes a float n
    as an argument and returns the floor of n
"""

from math import floor as fl


def floor(n: float) -> int:
    """ Returns the floor of the n """
    return fl(n)
