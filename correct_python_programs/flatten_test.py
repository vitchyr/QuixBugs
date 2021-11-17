from .flatten import flatten

def main():
    assert list(flatten([[1, [], [2, 3]], [[4]], 5])) == [1, 2, 3, 4, 5]
    assert list(flatten([1, [2, [3], []], 4, [[]], [5], 6])) == [1, 2, 3, 4, 5, 6]

if __name__ == "__main__":
    main()
