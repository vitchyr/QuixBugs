from .hanoi import hanoi


def test_main():
    assert hanoi(1, start=1, end=2) == [(1, 2)]
    assert hanoi(3, start=1, end=2) == [(1, 2), (1, 3), (2, 3), (1, 2), (3, 1), (3, 2), (1, 2)]
    assert hanoi(4, start=2, end=3) == [
        (2, 1),
        (2, 3),
        (1, 3),
        (2, 1),
        (3, 2),
        (3, 1),
        (2, 1),
        (2, 3),
        (1, 3),
        (1, 2),
        (3, 2),
        (1, 3),
        (2, 1),
        (2, 3),
        (1, 3)
    ]


if __name__ == "__main__":
    test_main()
