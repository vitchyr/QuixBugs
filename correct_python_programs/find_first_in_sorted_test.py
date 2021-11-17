from .find_first_in_sorted import find_first_in_sorted

def main():
    assert find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2
    assert find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 4) == 1
    assert find_first_in_sorted([1, 2, 3], 1) == 0
    assert find_first_in_sorted([], 1) == -1

if __name__ == "__main__":
    main()
