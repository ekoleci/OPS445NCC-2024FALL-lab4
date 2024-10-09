#!/usr/bin/env python3

def dictionary_to_string(my_dict):
    return ', '.join([f"{key}:{value}" for key, value in my_dict.items()])

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def invert_dictionary(my_dict):
    return {v: k for k, v in my_dict.items()}
