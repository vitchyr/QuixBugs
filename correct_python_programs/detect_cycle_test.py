from .node import Node
from .detect_cycle import detect_cycle


def main():
    # Case 1: 5-node list input with no cycle
    # Expected Output: Cycle not detected!
    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    node5 = Node(5, node4)

    assert not detect_cycle(node5)

    # Case 2: 5-node list input with cycle
    # Expected Output: Cycle detected!
    node1.successor = node5

    assert detect_cycle(node5)

    # Case 3: 2-node list with cycle
    # Expected Output: Cycle detected!
    node1.successor = node2

    assert detect_cycle(node2)

    # Case 4: 2-node list with no cycle
    # Expected Output: Cycle not detected!
    node6 = Node(6)
    node7 = Node(7, node6)

    assert not detect_cycle(node7)

    # Case 5: 1-node list
    # Expected Output: Cycle not detected!
    node = Node(0)
    assert not detect_cycle(node)

if __name__ == "__main__":
    main()
