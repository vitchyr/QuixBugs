from .sieve import sieve

def main():
    assert sieve(3) == [2, 3]
    assert sieve(4) == [2, 3]
    assert sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert sieve(1) == []
    assert sieve(43) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

if __name__ == "__main__":
    main()
