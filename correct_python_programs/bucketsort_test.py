from .bucketsort import bucketsort


def main():
    assert bucketsort([2, 1, 1, 1, 2], 5) == [1, 1, 1, 2, 2]
    assert bucketsort([4, 2, 1, 3, 4], 5) == [1, 2, 3, 4, 4]
    assert bucketsort([1], 2) == [1]


if __name__ == "__main__":
    main()
