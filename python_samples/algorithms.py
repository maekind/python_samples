#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" algorithms and data structure operations """

# SEARCHING


def search_employees_manager(employee, managers):
    """ Search the employee's manager in a dictionary """
    # The dictionary is a manager:[employees] key-value pair.
    employee_cleaned = employee.strip().lower().title()
    for manager, employees in managers.items():
        if employee_cleaned in employees:
            return manager

    return None
    # This is an O(n) complexity function in the worst case.

# SWAPPING


def swap_dict_a_b_values(values):
    """ Swap a b values in a dictionary without using variables """
    try:
        values['a'], values['b'] = values['b'], values['a']
    except (IndexError, TypeError, KeyError) as error:
        print(error)

    return values


def swap_dict_positions(values, pos1, pos2):
    """ Swap two positions in a dictionary """
    try:
        # Convert values to list
        tuple_values = list(values.items())

        # Swap positions, as in swap_dict_a_b_values
        tuple_values[pos1], tuple_values[pos2] = tuple_values[pos2], tuple_values[pos1]

        # Convert back to a dictionary
        values = dict(tuple_values)
    except (TypeError, IndexError) as error:
        print(error)

    return values
