def knapsack_dp(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, 0, -1):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

n = int(input("Enter the number of items: "))
capacity = int(input("Enter the knapsack capacity: "))

values, weights = [], []
for i in range(n):
    v, w = map(int, input(f"Enter value and weight for item {i + 1}: ").split())
    values.append(v)
    weights.append(w)

max_value = knapsack_dp(values, weights, capacity)
print(f"The maximum value that can be obtained is: {max_value}")
