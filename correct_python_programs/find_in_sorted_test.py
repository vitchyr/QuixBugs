from .find_in_sorted import find_in_sorted

def main():
    for lst, value in [
        ([3, 4, 5, 5, 5, 5, 6], 5),
        ([4, 5, 6], 5),
        ([4, 6], 5),
        ([], 5),
    ]:
        idx = find_in_sorted(lst, value)
        if idx == -1:
            assert value not in lst
        else:
            assert lst[idx] == value

if __name__ == "__main__":
    main()
