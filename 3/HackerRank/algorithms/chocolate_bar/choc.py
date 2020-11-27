from typing import List



# splitter attempts to break the list up into as equitable split as possible.
def splitter(bar: List[int], groups: int) -> List[int]:
    if len(bar) <= groups:
        raise ArithmeticError("%s is greater than the length of the bar (%d) provided"% (groups, len(bar)))

