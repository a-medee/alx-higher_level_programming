#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ A function that divides element by element 2 lists.

    Args:
        my_list_1: a list object
        my_list_2: a list object
        list_length: an int object

    Return:
        a new list object with all divisions
    """
    new_list = list()

    if my_list_1 is not None and my_list_2 is not None and \
       list_length >= 0 :

        for i in range(list_length):
            try:
                new_list.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except IndexError:
                new_list.append(0)
                print("out of range")
            finally:
                pass
    return new_list
