from .next_permutation import next_permutation


def test_main():
    assert next_permutation([3, 2, 4, 1]) == [3, 4, 1, 2]
    assert next_permutation([2, 4, 1]) == [4, 1, 2]


if __name__ == "__main__":
    test_main()
