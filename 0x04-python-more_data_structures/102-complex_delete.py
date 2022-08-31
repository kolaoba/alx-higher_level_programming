#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    deletes keys with a specific value in a dictionary.
    """
    if value not in a_dictionary.values():
        return a_dictionary
    new_dict = {}
    for key in a_dictionary.keys():
        if a_dictionary[key] != value:
            new_dict[key] = a_dictionary[key]
    return new_dict
