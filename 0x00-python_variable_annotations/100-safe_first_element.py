#!/usr/bin/env python3
""" Duck typing - duck-typed annotation """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# The types of input elements are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return first element """
    if lst:
        return lst[0]
    else:
        return None
