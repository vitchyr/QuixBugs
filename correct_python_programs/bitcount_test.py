from .bitcount import bitcount

"""
Driver to test bitcount
"""
def main():
    assert bitcount(127) == 7
    assert bitcount(128) == 1

if __name__ == "__main__":
    main()
