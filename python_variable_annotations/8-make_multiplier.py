#!/usr/bin/env python3
"""8-make_multiplier.py"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """documented"""
    return lambda float_val: float_val * multiplier
