from .gcd import gcd


def test_main():
    assert gcd(35, 21) == 7
    assert gcd(17, 21) == 1
    assert gcd(12, 6) == 6


if __name__ == "__main__":
    test_main()
