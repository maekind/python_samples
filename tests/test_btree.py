""" Test for algorithms methods """
from python_samples.binary_tree import BinaryTreeNode


def get_btree_sample() -> BinaryTreeNode:
    """ Method that returns a btree sample for testing """
    root = BinaryTreeNode(35)
    root.insert(25)
    root.insert(3)
    root.insert(56)

    return root


def test_new_node():
    """ Creating a node """
    new_node = BinaryTreeNode(40)
    assert str(new_node) == '40'


def test_insert_node():
    """ Inserting a node """
    try:
        new_node = BinaryTreeNode(40)
        new_node.insert(25)
    except Exception as error:
        raise error

    assert True


def test_search_existant_node_value():
    """ Searching an existing node value """
    root = get_btree_sample()
    assert root.search(root, 3) is True


def test_search_non_existant_node_value():
    """ Searching a non existing node value """
    root = get_btree_sample()
    assert root.search(root, 10) is False


def test_in_order_traversal():
    """ Test in_order_traversal method
        Traversal order: Left->Root->Right """
    root = get_btree_sample()
    expect_result = [3, 25, 35, 56]

    assert expect_result == root.in_order_traversal(root)


def test_pre_order_traversal():
    """ Test pre_order_traversal method
        Traversal pre-order: Root->Left->Right """
    root = get_btree_sample()
    expect_result = [35, 25, 3, 56]

    assert expect_result == root.pre_order_traversal(root)


def test_post_order_traversal():
    """ Test post_order_traversal method
        Traversal post-order: Left->Right->Root """
    root = get_btree_sample()
    expect_result = [3, 25, 56, 35]

    assert expect_result == root.post_order_traversal(root)
