#!/usr/bin/env python3
"""
    Given the parameters and the return values, add type annotations to
    the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""


from typing import TypeVar, Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[TypeVar('T'), None] = None) -> \
                             Union[Any, TypeVar('T')]:
    """Annotations added"""
    if key in dct:
        return dct[key]
    else:
        return default
