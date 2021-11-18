from .subsequences import subsequences

def main():
    assert subsequences(a=-1, b=3, k=3) == [[-1, 0, 1], [-1, 0, 2], [-1, 1, 2], [0, 1, 2]]
    assert subsequences(a=-1, b=3, k=4) == [[-1, 0, 1, 2]]
    assert subsequences(a=4, b=3, k=4) == []
    assert subsequences(a=4, b=3, k=1) == []
    assert subsequences(a=2, b=5, k=1) == [[2], [3], [4]]
    assert subsequences(a=1, b=5, k=3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]

if __name__ == "__main__":
    main()
