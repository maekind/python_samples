#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Contains classes for implementing a binary tree """

__package_name__ = "python_samples"
__authors__ = "Marco Espinosa"
__license__ = "MIT License"
__version__ = "1.0"
__maintainer__ = "Marco Espinosa"
__email__ = "hi@marcoespinosa.es"
__status__ = "Development"

from typing import List
from typing_extensions import Self


class BinaryTreeNode:
    """
    Implementation of a tree node for a binary tree.
    A node can have a value and a left node and/or a right node.
    How does it works? A binary tree is an ordered tree which grows
    in ascendant mode. So, the root is the smaller value and greater
    values are saved in to the right nodes.
    """

    def __init__(self, data) -> None:
        # Node value
        self.data = data
        # Right child
        self.right_child = None
        # Left child
        self.left_child = None

    def __str__(self) -> str:
        """" String representation of the Node class """
        return str(self.data)

    def __repr__(self) -> str:
        """ Readable representation of the Node class """
        return str(self.data)

    def insert(self, data):
        """
        Creates a new node with the given value:
        - If data is smaller than current node data:
            + If the left node is None, we create a new left node
            with new data.
            + Else if the left node exists, we add the data in to
            the left node.
        - If data is greater than current node data:
            + We perform the same operation as before but within the
            right node.
        """
        if self.data:

            if data < self.data:
                if self.left_child is None:
                    self.left_child = BinaryTreeNode(data)
                else:
                    self.left_child.insert(data)
            elif data > self.data:
                if self.right_child is None:
                    self.right_child = BinaryTreeNode(data)
                else:
                    self.right_child.insert(data)
        else:
            self.data = data

    def print(self):
        """ Print nodes recursively """
        if self.left_child:
            self.left_child.print()

        print(self.data, end=' ')

        if self.right_child:
            self.right_child.print()

    def in_order_traversal(self, root: Self) -> List:
        """ Traversal order: Left->Root->Right """
        res = []
        if root:
            res = self.in_order_traversal(root.left_child)
            res.append(root.data)
            res += self.in_order_traversal(root.right_child)

        return res

    def pre_order_traversal(self, root: Self) -> List:
        """ Traversal pre-order: Root->Left->Right """
        res = []
        if root:
            res.append(root.data)
            res += self.pre_order_traversal(root.left_child)
            res += self.pre_order_traversal(root.right_child)

        return res

    def post_order_traversal(self, root: Self) -> List:
        """ Traversal post-order: Left->Right->Root """
        res = []
        if root:
            res = self.post_order_traversal(root.left_child)
            res += self.post_order_traversal(root.right_child)
            res.append(root.data)

        return res

    def search(self, root: Self, data):
        """ Search data in the binary tree """
        if root is not None:
            if root.data == data:
                return True

            if data < root.data:
                return self.search(root.left_child, data)
            elif data > root.data:
                return self.search(root.right_child, data)

        return False


def print_btree(root): # pragma: no cover
    """ Generic B-tree test printing """
    print('Print: ', end=' ')
    root.print()
    print('')
    print('')

    print('Print in order: ', end=' ')
    print(root.in_order_traversal(root))
    print('')

    print('Print in pre order: ', end=' ')
    print(root.pre_order_traversal(root))
    print('')

    print('Print in post order: ', end=' ')
    print(root.post_order_traversal(root))
    print('')


def print_tree_numbers(): # pragma: no cover
    """ Printing a tree """
    root = BinaryTreeNode(3)
    root.insert(6)
    root.insert(2)
    root.insert(9)
    root.insert(10)

    print_btree(root)


def print_tree_names(): # pragma: no cover
    """ Printing a tree """
    root = BinaryTreeNode('Joe')
    root.insert('Alice')
    root.insert('Peter')
    root.insert('Bob')

    print_btree(root)


def main():
    """ Main method """
    print_tree_numbers()
    print_tree_names()


# main execution
if __name__ == "__main__":
    main()
