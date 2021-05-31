#!/usr/bin/env python3
"""
annotate a fn paramaters
"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    list of tuples for each elements and their length
    """
    return [(i, len(i)) for i in lst]
