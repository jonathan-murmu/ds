def coin_change(coins, no_of_coins, target):
    """Coin change.

    :param coins: The given collection of coins.
    :param no_of_coins: No of Coins
    :param target: The given amount
    :return: number of possible ways to make change for N cents.
    """

    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = [[0 for x in range(no_of_coins)] for x in range(target + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(no_of_coins):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, target + 1):
        for j in range(no_of_coins):
            # Count of solutions including coins[j]
            if i - coins[j] >= 0:
                x = table[i - coins[j]][j]
            else:
                x = 0

            # Count of solutions excluding coins[j]
            if j >= 1:
                y = table[i][j - 1]
            else:
                y = 0

            # total count
            table[i][j] = x + y

    return table[target][no_of_coins - 1]


if __name__ == "__main__":
    result = []
    test_cases = int(input())
    for test_case in range(test_cases):
        no_of_coins = int(input())
        coins = list(map(int, input().split()))
        target = input()
        result.append(coin_change(coins, no_of_coins, target))

    print('\n'.join(map(str, result)))