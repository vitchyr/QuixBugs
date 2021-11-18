from .shortest_path_lengths import shortest_path_lengths


def test_main():
    inf = float('inf')

    # Case 1: Basic graph input.
    # Output:
    graph = {
        (0, 2): 3,
        (0, 5): 5,
        (2, 1): -2,
        (2, 3): 7,
        (2, 4): 4,
        (3, 4): -5,
        (4, 5): -1
    }
    result = shortest_path_lengths(6, graph)
    expected = {
        (0, 0): 0,
        (0, 1): 1,
        (0, 2): 3,
        (0, 3): 10,
        (0, 4): 5,
        (0, 5): 4,
        (1, 0): inf,
        (1, 1): 0,
        (1, 2): inf,
        (1, 3): inf,
        (1, 4): inf,
        (1, 5): inf,
        (2, 0): inf,
        (2, 1): -2,
        (2, 2): 0,
        (2, 3): 7,
        (2, 4): 2,
        (2, 5): 1,
        (3, 0): inf,
        (3, 1): inf,
        (3, 2): inf,
        (3, 3): 0,
        (3, 4): -5,
        (3, 5): -6,
        (4, 0): inf,
        (4, 1): inf,
        (4, 2): inf,
        (4, 3): inf,
        (4, 4): 0,
        (4, 5): -1,
        (5, 0): inf,
        (5, 1): inf,
        (5, 2): inf,
        (5, 3): inf,
        (5, 4): inf,
        (5, 5): 0,
    }
    assert set(expected.keys()) == set(result.keys())
    for k in expected:
        assert result[k] == expected[k]

    # Case 2: Linear graph input.
    # Output:
    graph2 = {
        (0, 1): 3,
        (1, 2): 5,
        (2, 3): -2,
        (3, 4): 7
    }
    result = shortest_path_lengths(5, graph2)
    expected = {
        (0, 0): 0,
        (0, 1): 3,
        (0, 2): 8,
        (0, 3): 6,
        (0, 4): 13,
        (1, 0): inf,
        (1, 1): 0,
        (1, 2): 5,
        (1, 3): 3,
        (1, 4): 10,
        (2, 0): inf,
        (2, 1): inf,
        (2, 2): 0,
        (2, 3): -2,
        (2, 4): 5,
        (3, 0): inf,
        (3, 1): inf,
        (3, 2): inf,
        (3, 3): 0,
        (3, 4): 7,
        (4, 0): inf,
        (4, 1): inf,
        (4, 2): inf,
        (4, 3): inf,
        (4, 4): 0,
    }
    assert set(expected.keys()) == set(result.keys())
    for k in expected:
        assert result[k] == expected[k]

    # Case 3: Disconnected graphs input.
    # Output:
    graph3 = {
        (0, 1): 3,
        (2, 3): 5
    }
    result = shortest_path_lengths(4, graph3)
    expected = {
        (0, 0): 0,
        (0, 1): 3,
        (0, 2): inf,
        (0, 3): inf,
        (1, 0): inf,
        (1, 1): 0,
        (1, 2): inf,
        (1, 3): inf,
        (2, 0): inf,
        (2, 1): inf,
        (2, 2): 0,
        (2, 3): 5,
        (3, 0): inf,
        (3, 1): inf,
        (3, 2): inf,
        (3, 3): 0,
    }
    assert set(expected.keys()) == set(result.keys())
    for k in expected:
        assert result[k] == expected[k]

    # Case 4: Strongly connected graph input.
    graph4 = {
        (0, 1): 3,
        (1, 2): 5,
        (2, 0): -1
    }
    result = shortest_path_lengths(3, graph4)
    expected = {
        (0, 0): 0,
        (0, 1): 3,
        (0, 2): 8,
        (1, 0): 4,
        (1, 1): 0,
        (1, 2): 5,
        (2, 0): -1,
        (2, 1): 2,
        (2, 2): 0,
    }
    assert set(expected.keys()) == set(result.keys())
    for k in expected:
        assert result[k] == expected[k]


if __name__ == "__main__":
    test_main()
