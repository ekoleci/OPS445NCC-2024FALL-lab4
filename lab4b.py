#!/usr/bin/env python3

def list_starts_with(my_list, char):
    return [item for item in my_list if item.startswith(char)]

def sort_list(my_list):
    return sorted(my_list)

def list_to_string(my_list):
    return ','.join(my_list)
