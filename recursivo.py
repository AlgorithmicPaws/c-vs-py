import timeit

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def main():
    num = int(input("Enter a number to calculate its factorial: "))

    # Measure execution time using timeit
    execution_time_seconds = timeit.timeit(lambda: factorial(num), number=1)
    execution_time_microseconds = execution_time_seconds * 1e6  # Convert seconds to microseconds

    result = factorial(num)
    
    print(f"The factorial of {num} is: {result}")
    print(f"Execution time: {execution_time_microseconds:.2f} microseconds")

if __name__ == "__main__":
    main()
