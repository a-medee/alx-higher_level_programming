def roman_to_int(roman_string):
    """A function that converts a Roman numeral to an integer.

    Args:
        roman_string: a string object

    Returns:
        an int value
    """

    if roman_string is None or type(roman_string) != str:
        return 0

    
