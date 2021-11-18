from .possible_change import possible_change


def main():
    assert possible_change([1, 5, 10, 25], 11) == 4
    assert possible_change([1, 2, 3], 11) == 16
    assert possible_change([1], 123) == 1


if __name__ == "__main__":
    main()
