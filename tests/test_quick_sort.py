""" Test for Quicksort algorithm """
from python_samples.quick_sort import QuickSort

def test_sorted_array_in_ascendant_order():
    """ Method to test the quicksort implementation.
        The result has to be an ordered array in ascendant order """

    unsorted = [1, 7, 4, 1, 10, 23, 9, -2]
    expected = [-2, 1, 1, 4, 7, 9, 10, 23]

    # Quicksort instance
    qci = QuickSort(unsorted)
    qci.run()

    assert expected == qci.data
    