from .to_base import to_base

def main():
    assert to_base(31, 2) == '11111'
    assert to_base(32, 2) == '100000'
    assert to_base(32, 4) == '200'
    assert to_base(32, 13) == '26'
    assert to_base(432, 7) == '1155'
    assert to_base(31, 16) == '1F'


if __name__ == "__main__":
    main()
