from .pascal import pascal

def main():
    assert pascal(1) == [[1]]
    assert pascal(2) == [[1], [1, 1]]
    assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

if __name__ == "__main__":
    main()
