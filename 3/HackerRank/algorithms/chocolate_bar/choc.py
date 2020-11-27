from typing import List
from absl import logging
from copy import copy
from statistics import median_grouped


# splitter attempts to break the list up into as equitable split as possible.
def splitter(bar: List[int], groups: int) -> List[int]:
    forward_answer = _split(copy(bar),groups)
    reverse_answer = _split(copy(bar)[::-1],groups)
    if median_grouped(forward_answer) < median_grouped(reverse_answer):
        return forward_answer
    return reverse_answer

def _split(bar: List[int], groups: int) -> List[int]:
    if groups > len(bar):
        raise ArithmeticError("%s is greater than the length of the bar (%d) provided"% (groups, len(bar)))
    while len(bar) != groups:
        min_index = bar.index(min(bar))
        if min_index == 0:
            min_neighbor_index = 1
        elif min_index == len(bar)-1 or bar[min_index-1] <=  bar[min_index+1] :
            min_neighbor_index = min_index-1
        else:
            min_neighbor_index=min_index+1
        bar[min_neighbor_index] +=  bar[min_index]   
        del bar[min_index]
    return bar