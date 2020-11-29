from typing import List
from copy import deepcopy
import logging


def rotate_return(input: List[List[int]]) -> List[List[int]]:
    output = []
    for i in range(len(input)):
        line = list()
        for row in input:
            line.append(row[i])
        line.reverse()
        output.append(line)
    return output
