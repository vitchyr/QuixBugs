from .kth import kth


def test_main():
    assert kth([1, 2, 3, 4, 5], 0) == 1
    assert kth([5, 4, 3, 2, 1], 0) == 1
    assert kth([2, 3, 4, 5], 0) == 2
    assert kth([5, 4, 3, 2], 0) == 2
    assert kth([1], 0) == 1
    assert kth([5, 4, 3, 2], 3) == 5
    assert kth([5, 4, 3, 2, 1], 3) == 4
    assert kth([3, 4, 2, 5], 1) == 3
    assert kth([3, 4, 2, 5, 1], 1) == 2
    assert kth([3, 4, 2, 5], 3) == 5
    assert kth([3, 4, 2, 5, 1], 3) == 4


if __name__ == "__main__":
    test_main()
