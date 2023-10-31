def fibonacci(n, step_count=0):
    step_count += 1
    if n <= 0:
        return 0, step_count
    elif n == 1:
        return 1, step_count
    else:
        fib_1, step_count = fibonacci(n - 1, step_count)
        fib_2, step_count = fibonacci(n - 2, step_count)
        return fib_1 + fib_2, step_count

n = int(input("Enter the Fibonacci number you want to calculate: "))
fib_result, steps = fibonacci(n)
print(f"Fibonacci({n}) = {fib_result}")
print(f"Step count: {steps}")
