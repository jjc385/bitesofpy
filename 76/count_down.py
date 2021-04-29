from functools import singledispatch
from typing import Union, Sequence


@singledispatch
def count_down(data_type):
    raise ValueError("Unknown argument type")

@count_down.register
def _count_down(data: str):
    for i in range(len(data), 0, -1):
        print(data[:i])

def _count_down_numeric(data: Union[int, float]):
    return count_down(str(data))

def _count_down_sequence(data: Sequence):
    return count_down("".join(str(x) for x in data))

@count_down.register
def _count_down(data: int):
    return _count_down_numeric(data)

@count_down.register
def _count_down(data: float):
    return _count_down_numeric(data)

@count_down.register
def _count_down(data: list):
    return _count_down_sequence(data)

@count_down.register
def _count_down(data: tuple):
    return _count_down_sequence(data)

@count_down.register
def _count_down(data: dict):
    return count_down(list(data))

@count_down.register
def _count_down(data: set):
    return count_down(sorted(data))

@count_down.register
def _count_down(data: range):
    return _count_down_sequence(data)

