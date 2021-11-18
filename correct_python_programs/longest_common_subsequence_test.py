from .longest_common_subsequence import longest_common_subsequence

def main():
    assert longest_common_subsequence('headache', 'pentadactyl') == 'eadac'
    assert longest_common_subsequence('', 'pentadactyl') == ''
    assert longest_common_subsequence('a', 'aaa') == 'a'
    assert longest_common_subsequence('aa', 'aaa') == 'aa'
    assert longest_common_subsequence('abc', 'aabc') == 'abc'
    assert longest_common_subsequence('aabc', 'abc') == 'abc'

if __name__ == "__main__":
    main()
