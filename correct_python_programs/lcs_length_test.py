from .lcs_length import lcs_length


def main():
    assert lcs_length('witch', 'sandwich') == 2
    assert lcs_length('meow', 'homeowner') == 4
    assert lcs_length('aaa', 'baaa') == 3
    assert lcs_length('aaa', 'aaab') == 3
    assert lcs_length('aaa', 'aaa') == 3
    assert lcs_length('bab', 'a') == 1
    assert lcs_length('a', 'bab') == 1
    assert lcs_length('aa', 'baab') == 2
    assert lcs_length('ba', 'a') == 1
    assert lcs_length('ab', 'a') == 1


if __name__ == "__main__":
    main()
