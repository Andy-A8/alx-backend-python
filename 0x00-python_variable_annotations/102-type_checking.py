#!/usr/bin/env Python3
"""
    Use mypy to validate the following piece of code and apply
    any necessary changes
"""


from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Fixed annotations"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return (zoomed_in)


array = (12, 72, 91)  # Used tuple instead of list

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Used integer instead of float
