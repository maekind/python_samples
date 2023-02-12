#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Contains classes for implementing a custom linked list """

__package_name__ = "python_samples"
__authors__ = "Marco Espinosa"
__license__ = "MIT License"
__version__ = "1.0"
__maintainer__ = "Marco Espinosa"
__email__ = "hi@marcoespinosa.es"
__status__ = "Development"
__name__ = "Custom_Linked_List"


class NodeNotFoundException(BaseException):
    """ Node not found exception class"""


class Node:
    """ Class to handle linked node implementation """

    def __init__(self, data: object) -> None:
        """
        Default constructor.
        param data: data value to assign to the current node. """

        self._data = data
        self._next = None

    def __repr__(self) -> str:
        """ String representation of a node """
        return str(self._data)

    @property
    def data(self) -> object:
        """ data getter accessor """
        return self._data

    @data.setter
    def data(self, value) -> None:
        """ data setter accessor """
        self._data = value

    @property
    def next(self):
        """ next getter accessor """
        return self._next

    @next.setter
    def next(self, value) -> None:
        """ next setter accessor """
        self._next = value


class CustomLinkedList:
    """ Class to implement a custom linked list """

    def __init__(self, nodes: list = None) -> None:
        """
        Default constructor.
        param nodes: list of data objects for creating nodes.
        """
        if nodes is not None:
            # Set the first node to the head list
            node = Node(nodes.pop(0))
            self.head = node

            # For the rest of nodes, create node an link to the next
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def __repr__(self) -> str:
        """ String representation for the CustomLinkedList class """
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")

        return " -> ".join(nodes)

    def __iter__(self) -> Node:
        """ Node iterator """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, data: object) -> None:
        """
        Adds new node with data value at the beginning.
        param data: data object for the new node.
        """

        if data is not None:
            node = Node(data=data)

            if self.head is not None:
                node.next = self.head
                self.head = node
            else:
                self.head = node

    def add_last(self, data: object) -> None:
        """
        Adds new node with data value at the end.
        param data: data object for the new node.
        """
        if data is not None:
            node = Node(data=data)

            # Set pointer to the last node
            for current_node in self:
                pass

            # Set new last node
            if current_node is not None:
                current_node.next = node

    def add_after(self, targeted_data: object, new_data: object) -> None:
        """
        Adds new node with new_data value after the node with targeted_data value.
        param targeted_data: data object of an existing node.
        param new_data: data object for the new node.
        """

        if new_data is not None:
            node = Node(data=new_data)

            # Set pointer to the last node
            for current_node in self:
                if current_node.data == targeted_data:
                    node.next = current_node.next
                    current_node.next = node
                    return

            raise NodeNotFoundException(
                f"Targeted data {targeted_data} doesn't found!")

    def add_before(self, targeted_data: object, new_data: object) -> None:
        """
        Adds new node with new_data value before the node with targeted_data value.
        param targeted_data: data object of an existing node.
        param new_data: data object for the new node.
        """

        if new_data is not None:
            node = Node(data=new_data)
            previous_node = None

            for current_node in self:
                if previous_node is not None and \
                        current_node.data == targeted_data:

                    previous_node.next = node
                    node.next = current_node
                    return

                previous_node = current_node

            raise NodeNotFoundException(
                f"Targeted data {targeted_data} doesn't found!")

    def sort(self):
        """
        Method to sort the list ascendant
        NOTE: The best method is the merge sort algorithm.
        Merge sort algorithm splits in two equal lists the original list.
        Then, sorts each list individually. It sorts each list recursively,
        by dividing again each least in two equal parts. So, every time the
        the sort method is called, it is called with a smaller piece of list.
        Finally, the two resultant lists have to be merged.
        """

        try:
            self.head = self._sort(self.head)
        except Exception as error:
            raise TypeError("The list can not be sorted!") from error

    def _sort(self, node) -> None:
        """
        Auxiliary function to do the recursive work.
        param node: the head of the list to be sorted.
        """

        if node is None or node.next is None:
            return node

        # Get the middle node of the list beginning on node
        middle_node = self.get_middle_node(node)
        next_middle_node = middle_node.next
        # Point the middle node to None, so it does split the list in two parts
        middle_node.next = None
        # Sort left and right parts of the list recursively
        left_sorted_node = self._sort(node)
        right_sorted_node = self._sort(next_middle_node)

        # Return the merged list
        return self._merge_two_lists(left_sorted_node, right_sorted_node)

    def get_middle_node(self, node):
        """
        Auxiliary function to get the middle node of a list
        param node: node from which stating to find the node in the middle.
        """

        if node is None:
            return node

        slow_node = node
        fast_node = node.next

        # Move faster pointer by two, slower by one
        while fast_node is not None:
            fast_node = fast_node.next

            if fast_node is not None:
                fast_node = fast_node.next
                slow_node = slow_node.next

        return slow_node

    def _merge_two_lists(self, node_left, node_right):
        """
        Auxiliary function to merge two lists
        param a: node left
        param b: node right
        """

        if node_left is None:
            return node_right

        if node_right is None:
            return node_left

        head_of_merged_list = None
        temp_node_for_merged_list = None

        # Selecting the header (Always checking in ascendant mode)
        if node_left.data <= node_right.data:
            head_of_merged_list = node_left
            node_left = node_left.next
        else:
            head_of_merged_list = node_right
            node_right = node_right.next

        temp_node_for_merged_list = head_of_merged_list

        # Iterate through the two lists
        while node_left is not None and node_right is not None:

            if node_left.data <= node_right.data:
                temp_node_for_merged_list.next = node_left
                node_left = node_left.next
                temp_node_for_merged_list = temp_node_for_merged_list.next
                temp_node_for_merged_list.next = None

            else:
                temp_node_for_merged_list.next = node_right
                node_right = node_right.next
                temp_node_for_merged_list = temp_node_for_merged_list.next
                temp_node_for_merged_list.next = None

        # if "b" ends then we assign all remain elements of "a" to end of "head_of_merged_list",
        # if "a" ends then we assign all remain elements of "b" to end of "head_of_merged_list".
        # and then returns the "head_of_merged_list".

        if node_left is not None:
            temp_node_for_merged_list.next = node_left

        if node_right is not None:
            temp_node_for_merged_list.next = node_right

        return head_of_merged_list


def print_content(custom_list):
    """ Method for printing the custom list nodes """

    # TWO ways for printing list content:
    # Using __repr__ function that returns a formatted string representation
    print(f'Using __repr__ function: {str(custom_list)}')

    # Using __iter__ function that iterates list nodes
    print('Using __iter__ function: ', end='')
    for node in custom_list:
        print(f'{str(node)} -> ', end='')
    print('None')


def print_sorted_list(custom_list):
    """ Method for sorting and printing the list """
    custom_list.sort()
    print(f'Sorted list: {str(custom_list)}')


def check_add_nodes(custom_list):
    """ Method to check wheater a node exists or not """
    # Checking functions to add new nodes
    custom_list.add_first("1024")
    custom_list.add_last("8096")
    print(
        f'Added 1024 at the beginning and 8096 at the end: {str(custom_list)}')

    try:
        custom_list.add_after("5", "4092")
        print(f'Added 4092 after 5: {str(custom_list)}')
        # An exception will be raised because there is no 125 node!
        custom_list.add_after("125", "128")
    except NodeNotFoundException as error:
        print(f'Warning: {error}')

    try:
        custom_list.add_before("5", "2048")
        print(f'Added 2048 before 5: {str(custom_list)}')
        # An exception will be raised because there is no 125 node!
        custom_list.add_before("125", "128")
    except NodeNotFoundException as error:
        print(f'Warning: {error}')


def print_middle_node(custom_list):
    """ Method for printing the middle node """
    node = custom_list.get_middle_node(custom_list.head)
    print(f'Middle node: {node}')


def main():
    """ main method to retrieve console input """

    nodes = "a"
    while nodes != "e":
        nodes = input(
            "Enter a list of coma separated values: (type e to exit):")
        try:
            if nodes == "e":
                break

            if nodes != "":
                nodes = nodes.split(',')
                custom_list = CustomLinkedList(nodes)

                print_content(custom_list)

                print_sorted_list(custom_list)

                check_add_nodes(custom_list)

                print_middle_node(custom_list)

        except TypeError as error:
            print(error)
        except Exception as error:
            print(f"{error}. A list of coma separated values is expected!")


# main execution
if __name__ == "__main__":
    main()
