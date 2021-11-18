from .wrap import wrap


def test_main():
    assert wrap('abcdefgh', 2) == ['ab', 'cd', 'ef', 'gh']
    assert wrap('abcdefghi', 2) == ['ab', 'cd', 'ef', 'gh', 'i']
    assert wrap('abcdefghi', 1) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    assert wrap('abcdefghi', 13) == ['abcdefghi']
    assert wrap('abcdefghi', 9) == ['abcdefghi']
    assert wrap('abcdefghi', 8) == ['abcdefgh', 'i']


if __name__ == "__main__":
    test_main()
