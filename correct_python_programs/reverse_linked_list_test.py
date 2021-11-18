from .node import Node
from .reverse_linked_list import reverse_linked_list


def main():
    # Case 1: 5-node list input
    # Expected Output: 1 2 3 4 5
    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    node5 = Node(5, node4)

    result = reverse_linked_list(node5)

    full_results = []
    while result:
        full_results.append(result.value)
        result = result.successor
    assert full_results == [1, 2, 3, 4, 5]

    # Case 2: 1-node list input
    # Expected Output: 0
    node = Node(0)
    result = reverse_linked_list(node)

    full_results = []
    while result:
        full_results.append(result.value)
        result = result.successor
    assert full_results == [0]

    # Case 3: None input
    # Expected Output: None
    result = reverse_linked_list(None)
    assert result == None


if __name__ == "__main__":
    main()
