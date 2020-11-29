import logging


def compress(input: str) -> str:
    last, last_count = input[0], 1
    output = ''
    for letter in input[1:]:
        if last == letter:
            last_count += 1
        else:
            output += "%s%d" % (last, last_count)
            last_count = 1
        last = letter
    output += "%s%d" % (last, last_count)
    if len(input) < len(output):
        return input
    return output
