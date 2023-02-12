#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This file contains the Quicksort algorithm implementation """


class QuickSort():
    """ This implementation utilizes pivot as the last element in the nums list
    It has a pointer to keep track of the elements smaller than the pivot
    At the very end of partition() function, the pointer is swapped with the pivot
    to come up with a "sorted" nums relative to the pivot """

    def __init__(self, array):
        """ Default constructors

            params:
                @array: Array of numbers
        """

        self._data = array

    def run(self):
        """ Launches quicksort algorithm """
        self._quick_sort(self._data, 0, len(self._data) - 1)

    def _partition(self, array, low, high):
        """ Function to find the partition position """

        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:

                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # Return the position from where partition is done
        return i + 1

    def _quick_sort(self, array, low, high):
        """ Function to perform the quicksort """
        if low < high:

            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pivot = self._partition(array, low, high)

            # Recursive call on the left of pivot
            self._quick_sort(array, low, pivot - 1)

            # Recursive call on the right of pivot
            self._quick_sort(array, pivot + 1, high)

    @property
    def data(self):
        """" Property data """
        return self._data


def main():
    """ Main function """

    unsorted = [1, 7, 4, 1, 10, 23, 9, -2]
    print(f"Unsorted Array: {unsorted}")

    # Quicksort instance
    qci = QuickSort(unsorted)
    qci.run()

    print(f'Sorted Array in Ascending Order: {qci.data}')


if __name__ == "__main__":
    main()
