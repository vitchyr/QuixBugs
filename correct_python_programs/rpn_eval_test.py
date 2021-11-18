from .rpn_eval import rpn_eval

def main():
    assert rpn_eval([3.0, 5.0, '+', 2.0, '/']) == 4.0
    assert rpn_eval([3.0, 5.0, '+', 2.0, '*']) == 16.0
    assert rpn_eval([1.0, 3.2, '+']) == 4.2

if __name__ == "__main__":
    main()
