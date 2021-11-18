from .sqrt import sqrt


def main():
    assert sqrt(2, 0.01) == 1.4166666666666665
    assert sqrt(3, 0.001) == 1.7321428571428572
    assert sqrt(4, 0) == 2.0
    assert sqrt(132, 0.01) == 11.489422513833343
    assert sqrt(132, 0.1) == 11.489422513833343
    assert sqrt(132, 1) == 11.489422513833343
    assert sqrt(123124, 0.1) == 350.8902962974845


if __name__ == "__main__":
    main()

