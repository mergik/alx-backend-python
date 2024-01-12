#!/usr/bin/env python3
"""
Function that annotates the test function parameters
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns values with the appropriate types"""
    return [(i, len(i)) for i in lst]
