#!/usr/bin/env python3
"""
add type annotations to the function
"""
from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    dct[key] if exists otherwise default
    """
    if key in dct:
        return dct[key]
    else:
        return default
