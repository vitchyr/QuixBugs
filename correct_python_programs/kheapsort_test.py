from .kheapsort import kheapsort


def main():
    assert list(kheapsort([3, 2, 1, 5, 4], 2)) == [1, 2, 3, 4, 5]
    assert list(kheapsort([5, 4, 3, 2, 1], 4)) == [1, 2, 3, 4, 5]
    assert list(kheapsort([1, 2, 3, 4, 5], 0)) == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()
