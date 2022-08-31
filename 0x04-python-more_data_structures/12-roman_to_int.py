#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    converts a Roman numeral to an integer.
    """
    if not roman_string:
        return 0
    hashMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arr = [hashMap[key] for key in roman_string]
    if len(arr) == 1:
        return arr[0]
    else:
        sum_ = arr[0]
        for idx in range(1, len(arr)):
            if arr[idx] <= arr[idx-1]:
                sum_ += arr[idx]
            else:
                sum_ -= arr[idx]
    return abs(sum_)
