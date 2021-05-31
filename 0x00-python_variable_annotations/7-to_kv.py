#!/usr/bin/env python3
"""
tuple of a string and a int/float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    tuple of k & v
    """
    return (k, v * v)
