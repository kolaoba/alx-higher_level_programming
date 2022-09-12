#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list

    Args:
        my_list (list): list to print elements from
        x (int): number of elements of my_list to be printed

    Returns:
        The number of elements printed
    """
    count = 0
    for idx in range(x):
        try:
            print(f"{my_list[idx]}", end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
