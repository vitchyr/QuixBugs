from .knapsack import knapsack


def test_main():
    assert knapsack(100, [(60, 10), (50, 8), (20, 4), (20, 4), (8, 3), (3, 2)]) == 19
    assert knapsack(0, [(60, 10), (50, 8), (20, 4), (20, 4), (8, 3), (3, 2)]) == 0
    assert knapsack(10, [(5, 1), (5, 1)]) == 2
    assert knapsack(10, []) == 0


if __name__ == "__main__":
    test_main()
