"""Function to calculate fib with use of recursion"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result


num_fib_vals = int(input("How many fib numbs you want to find? "))
i = 1
while i < num_fib_vals:
    fib_value= fib(i)
    print(fib_value)
    i += 1