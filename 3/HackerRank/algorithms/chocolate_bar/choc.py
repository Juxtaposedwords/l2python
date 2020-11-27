from typing import List
from absl import logging
from copy import copy
from statistics import stdev


# splitter attempts to break the list up into as equitable split as possible.
def splitter(bar: List[int], groups: int) -> List[int]:
    if groups > len(bar):
        raise ArithmeticError(
            "%s is greater than the length of the bar (%d) provided" %
            (groups, len(bar)))
    while len(bar) != groups:
        min_index = bar.index(min(bar))
        if min_index == 0:
            min_neighbor_index = 1
        elif min_index == len(bar) - 1:
            min_neighbor_index = len(bar) - 2
        elif bar[min_index - 1] == bar[min_index + 1] and stdev(
                bar[min_index:]) < stdev(bar[:min_index]):
            min_neighbor_index = min_index - 1
        elif bar[min_index - 1] == bar[min_index + 1]:
            min_neighbor_index = min_index + 1
        elif bar[min_index - 1] < bar[min_index + 1]:
            min_neighbor_index = min_index - 1
        else:
            min_neighbor_index = min_index + 1
        bar[min_neighbor_index] += bar[min_index]
        del bar[min_index]
    return bar
