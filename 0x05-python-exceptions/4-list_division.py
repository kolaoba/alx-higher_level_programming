#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element 2 lists.

    Arguments:
        my_list_1, my_list_2 (list(any type)): lists containing
                                            elements to be divided
        list_length (int): length of return list

    Returns:
        a new list with all divisions
    """
    new_list = []
    for idx in range(0, list_length):
        try:
            res = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
