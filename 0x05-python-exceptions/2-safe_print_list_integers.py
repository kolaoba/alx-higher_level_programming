#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers.

    Arguments:
        my_list (list(any type)): list of values to be printed
        x (int): number of elements to access in my_list

    Returns:
        The real number of integers printed
    """
    count = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
        except (ValueError, TypeError):
            continue
        else:
            count += 1
    print("")
    return count
