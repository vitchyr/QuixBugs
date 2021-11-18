from .powerset import powerset


def main():
    assert powerset(['a', 'b', 'c']) == [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]
    assert powerset([0, 1]) == [[], [1], [0], [0, 1]]
    assert powerset([]) == [[]]


if __name__ == "__main__":
    main()