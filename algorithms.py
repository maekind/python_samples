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

# Tests


def test_swap_dict_a_b_values():
    """ Pythonic dictionary values swapping """
    dict_one = {'a': 1, 'b': 2}
    expected_dict = {'a': 2, 'b': 1}

    assert swap_dict_a_b_values(dict_one) == expected_dict


def test_swap_dict_positions():
    """ Swap position of two items in a dictionary """
    dict_one = {'a': 1, 'b': 2, 'c': 3}
    expected_dict = {'c': 3, 'b': 2, 'a': 1}

    assert swap_dict_positions(dict_one, 0, 2) == expected_dict


def test_search_employees_manager():
    """ Search values in a dictionary """
    managers = {
        'Tom': ['Mary', 'Paul'],
        'Pepe': ['Juan'],
        'John': ['Truman', 'Ana', 'Atos'],
    }

    assert search_employees_manager('mary', managers) == 'Tom'
    assert search_employees_manager('gary', managers) is None
