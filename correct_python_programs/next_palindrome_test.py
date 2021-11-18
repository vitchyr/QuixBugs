from .next_palindrome import next_palindrome

def main():
    assert next_palindrome([1, 4, 9, 4, 1]) == [1, 5, 0, 5, 1]
    assert next_palindrome([9, 9]) == [1, 0, 1]
    assert next_palindrome([1]) == [2]
    assert next_palindrome([3, 2, 3]) == [3, 3, 3]

if __name__ == "__main__":
    main()
