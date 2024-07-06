#!/usr/bin/env python3
""" Advanced type annotations using TypeVar """
from typing import Mapping, Any, Sequence, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """ Get value using the key """
    if key in dct:
        return dct[key]
    else:
        return default
