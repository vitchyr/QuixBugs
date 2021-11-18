from .lis import lis

def main():
    assert lis([4, 1, 5, 3, 7, 6, 2]) == 3
    assert lis([1, 1, 1, 1]) == 1
    assert lis([]) == 0
    assert lis([3, 2, 1, 0]) == 1
    assert lis([1, 2, 3, 4]) == 4

if __name__ == "__main__":
    main()
