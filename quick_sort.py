# -*- coding: utf-8 -*-
#!/usr/bin/env python3
""" Python program for implementation of Quicksort Sort
This implementation utilizes pivot as the last element in the nums list
It has a pointer to keep track of the elements smaller than the pivot
At the very end of partition() function, the pointer is swapped with the pivot
to come up with a "sorted" nums relative to the pivot """


def partition(array, low, high):
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


def quick_sort(array, low, high):
    """ Function to perform the quicksort """
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pivot - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pivot + 1, high)


def test_sorted_array_in_ascendant_order():
    """ Method to test the quicksort implementation. 
        The result has to be an ordered array in ascendant order """

    unsorted = [1, 7, 4, 1, 10, 23, 9, -2]
    expected = [-2, 1, 1, 4, 7, 9, 10, 23]

    quick_sort(unsorted, 0, len(unsorted) - 1)

    assert expected == unsorted


def main():
    """ Main function """

    data = [1, 7, 4, 1, 10, 23, 9, -2]
    print(f"Unsorted Array: {data}")

    quick_sort(data, 0, len(data) - 1)

    print(f'Sorted Array in Ascending Order: {data}')


if __name__ == "__main__":
    main()
