from .node import Node
from .breadth_first_search import breadth_first_search


def test_main():
    # Case 1: Strongly connected graph
    # Output: Path found!
    station1 = Node("Westminster")
    station2 = Node("Waterloo", None, [station1])
    station3 = Node("Trafalgar Square", None, [station1, station2])
    station4 = Node("Canary Wharf", None, [station2, station3])
    station5 = Node("London Bridge", None, [station4, station3])
    station6 = Node("Tottenham Court Road", None, [station5, station4])

    assert breadth_first_search(station6, station1)

    # Case 2: Branching graph
    # Output: Path found!
    nodef = Node("F")
    nodee = Node("E")
    noded = Node("D")
    nodec = Node("C", None, [nodef])
    nodeb = Node("B", None, [nodee])
    nodea = Node("A", None, [nodeb, nodec, noded])

    assert breadth_first_search(nodea, nodee)

    # Case 3: Two unconnected nodes in graph
    # Output: Path not found
    assert not breadth_first_search(nodef, nodee)

    # Case 4: One node graph
    # Output: Path found!
    assert breadth_first_search(nodef, nodef)

    # Case 5: Graph with cycles
    # Output: Path found!
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4", None, [node1])
    node5 = Node("5", None, [node2])
    node6 = Node("6", None, [node5, node4, node3])

    node2.successors = [node6]
    assert breadth_first_search(node6, node1)


if __name__ == "__main__":
    test_main()
