from .mergesort import mergesort


def main():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert mergesort([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
    assert mergesort([3, 2, 5, 4, 1]) == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()
