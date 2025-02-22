from .levenshtein import levenshtein


def test_main():
    assert levenshtein('electron', 'neutron') == 3
    assert levenshtein('apples', 'dog') == 6
    assert levenshtein('apples', 'apple') == 1


if __name__ == "__main__":
    test_main()
