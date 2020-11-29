from typing import List
from copy import deepcopy
import logging


def rotate_return(input: List[List[int]]) -> List[List[int]]:
    output = []
    for i in range(len(input)):
        logging.error("i is %d", i)
        line = list()
        for row in input:
            logging.error("row: {} i {} entry: {}".format(row, i, row[i]))
            line.append(row[i])
        output.append(line)
        logging.error("line: {} ".format(line.reverse()))
    return output
