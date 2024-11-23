def min_coins(coins, amount):
    """
    Finds the minimum number of coins needed to make up a given amount using dynamic
    programming.
    This function solves the coin change problem by determining the fewest number of
    coins from a given set of coin denominations that sum up to a target amount. The
    solution uses dynamic programming (tabulation) to iteratively build up the minimum
    number of coins required for each amount.

    Parameters:
        coins (list of int): A list of coin denominations available for making change. Each
        coin denomination is a positive integer.
        amount (int): The target amount for which we need to find the minimum number of coins.
        It must be a non-negative integer.

    Returns:
        int: The minimum number of coins required to make the given amount.
        If it is not possible to make the amount with the given coins, returns -1.

    Example:
    >>> min_coins([1, 2, 5], 11)
    3
    >>> min_coins([2], 3)
    -1
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


