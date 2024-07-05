#!/usr/bin/env python3
""" Complex types - Takes in a List of floats """
from typing import Iterator, Union, Callable, Optional, List


def sum_list(input_list: List[float]) -> float:
    """
    Takes in a list input_list of floats as argument
    returns their sum as a float.
    """

    return sum(input_list)
