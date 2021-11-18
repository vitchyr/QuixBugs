from .is_valid_parenthesization import is_valid_parenthesization

def main():
    assert is_valid_parenthesization('((()()))()')
    assert is_valid_parenthesization('()')
    assert is_valid_parenthesization('')
    assert not is_valid_parenthesization(')()(')
    assert not is_valid_parenthesization('(()()')
    assert not is_valid_parenthesization('(())(()')

if __name__ == "__main__":
    main()
