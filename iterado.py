import timeit

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    num = int(input("Enter a number to calculate its factorial: "))

    # Measure execution time using timeit
    execution_time_seconds = timeit.timeit(lambda: factorial_iterative(num), number=1)
    execution_time_microseconds = execution_time_seconds * 1e6  # Convert seconds to microseconds

    result = factorial_iterative(num)
    
    print(f"The factorial of {num} is: {result}")
    print(f"Execution time: {execution_time_microseconds:.2f} microseconds")

if __name__ == "__main__":
    main()
