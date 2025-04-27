#!/usr/bin/env python3
"""7-to_kv.py"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """documented"""
    return (k, v * v)
