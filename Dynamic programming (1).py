def min_coins(coins, amount):
    """
    Finds the minimum number of coins needed to make up a given amount using dynamic programming.
    If it is not possible to make the amount, the function returns -1.

    Parameters:
        coins (list): A list of integers representing the denominations of the coins.
        amount (int): The target amount to be achieved.

    Returns:
        int: The minimum number of coins needed to make up the amount, or -1 if it's not possible.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
coins = [1, 2, 5]
amount = 11
result = min_coins(coins, amount)
print(result)

