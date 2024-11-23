def knapsack(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.

    Parameters:
        weights (list): A list of integers representing the weights of the items.
        values (list): A list of integers representing the values of the items.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        int: The maximum value that can be achieved within the given weight capacity.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w: 
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
result = knapsack(weights, values, capacity)
print(result)  
