#!/usr/bin/python3

def magic_calculation(a, b):
    """This function does a task

    Args:
        a: The first argument.
        b: The second argument.

    Returns:
        The result of the calculation.
  """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result = result + (a ** b / i)
        except Exception:
            result = a + b
            break
        finally:
            pass
    return result
