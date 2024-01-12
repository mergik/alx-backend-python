#!/usr/bin/env python3
"""
Type-annotated function that takes a string `k` and an int
OR float `v` as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing the input string
    and the square of the input int or float."""
    return (k, float(v) ** 2)
