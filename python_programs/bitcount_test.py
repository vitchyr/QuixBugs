from .bitcount import bitcount


def test_main():
    assert bitcount(127) == 7
    assert bitcount(128) == 1
    assert bitcount(1) == 1
    assert bitcount(0) == 0
    assert bitcount(30) == 4


if __name__ == "__main__":
    test_main()
