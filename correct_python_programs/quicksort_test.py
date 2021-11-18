from .quicksort import quicksort


def main():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quicksort([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
    assert quicksort([3, 2, 5, 4, 1]) == [1, 2, 3, 4, 5]
    assert quicksort([2, 5, 4, 1]) == [1, 2, 4, 5]
    assert quicksort([2, 2, 2, 1]) == [1, 2, 2, 2]


if __name__ == "__main__":
    main()