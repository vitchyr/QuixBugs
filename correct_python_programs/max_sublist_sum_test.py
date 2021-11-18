from .max_sublist_sum import max_sublist_sum


def test_main():
    assert max_sublist_sum([4, -5, 2, 1, -1, 3]) == 5
    assert max_sublist_sum([1, -1, 1, 1, -1, 1]) == 2
    assert max_sublist_sum([2, -1, 2, -2, 3, -3, 4]) == 5
    assert max_sublist_sum([-1, -1, -1]) == 0


if __name__ == "__main__":
    test_main()
