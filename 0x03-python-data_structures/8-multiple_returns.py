#!/usr/bin/python3

def multiple_returns(sentence):
    """A function that returns a tuple with the length of a string
       and its first character.

    Args:
        sentence: a tuple

    Returns:
        a tuple
    """

    if sentence:
        return len(sentence), sentence[0]
    return 0, None
