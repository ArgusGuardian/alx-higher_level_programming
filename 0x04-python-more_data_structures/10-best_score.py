#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        max = 0
        for key, value in a_dictionary.items():
            if a_dictionary[key] > max:
                max = a_dictionary[key]
                max_key = key
        return max_key
    return None
