def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value, remaining_capacity = 0, capacity

    for weight, value in items:
        fraction = min(1, remaining_capacity / weight)
        total_value += fraction * value
        remaining_capacity -= fraction * weight

    return total_value

n = int(input("Enter the number of items: "))
capacity = float(input("Enter the knapsack capacity: "))
items = []

for i in range(n):
    weight, value = map(float, input(f"Enter weight and value for item {i + 1}: ").split())
    items.append((weight, value))

max_value = fractional_knapsack(items, capacity)
print(f"The maximum value that can be obtained is: {max_value:.2f}")
