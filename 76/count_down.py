from functools import singledispatch
from typing import Union, Sequence


@singledispatch
def count_down(data_type):
    raise ValueError("Unknown argument type")

@count_down.register
def _count_down(data: str):
    for i in range(len(data), 0, -1):
        print(data[:i])

@count_down.register(int)
@count_down.register(float)
def _count_down_numeric(data: Union[int, float]):
    return count_down(str(data))

@count_down.register(list)
@count_down.register(tuple)
@count_down.register(dict)
@count_down.register(range)
def _count_down_sequence(data: Sequence):
    return count_down("".join(str(x) for x in data))

@count_down.register
def _count_down(data: set):
    return count_down(sorted(data))

