""" Test for algorithms methods """
from python_samples.algorithms import *

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
