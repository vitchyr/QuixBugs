from .get_factors import get_factors


def test_main():
    assert get_factors(1) == []
    assert get_factors(100) == [2, 2, 5, 5]
    assert get_factors(101) == [101]


if __name__ == "__main__":
    test_main()
