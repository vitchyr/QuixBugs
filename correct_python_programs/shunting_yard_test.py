from .shunting_yard import shunting_yard

def main():
    assert shunting_yard([10, '-', 5, '-', 2]) == [10, 5, '-', 2, '-']
    assert shunting_yard([34, '-', 12, '/', 5]) == [34, 12, 5, '/' ,'-']
    assert shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13]) == [4, 9, 9, '*', '+', 10, '-', 13, '+']

if __name__ == "__main__":
    main()
