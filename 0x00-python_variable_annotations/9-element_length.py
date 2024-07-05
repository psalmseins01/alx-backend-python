#!/usr/bin/env python3
""" Type annotation for function 'element_length'"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length function """
    return [(i, len(i)) for i in lst]
