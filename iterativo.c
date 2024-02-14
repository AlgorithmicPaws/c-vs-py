#include <stdio.h>
#include <time.h>

long long factorial(int n) {
    long long result = 1;
    for (long long i = 1; i <= n; ++i) {
        result *= i;
    }
    return result;
}

int main() {
    int num;
    printf("Enter a number to calculate its factorial: ");
    scanf("%d", &num);

    struct timespec start_time, end_time;
    clock_gettime(CLOCK_REALTIME, &start_time); // Get start time

    long long result = factorial(num);

    clock_gettime(CLOCK_REALTIME, &end_time); // Get end time

    // Calculate elapsed time in microseconds
    long long start_nanoseconds = start_time.tv_sec * 1000000000 + start_time.tv_nsec;
    long long end_nanoseconds = end_time.tv_sec * 1000000000 + end_time.tv_nsec;
    long long elapsed_nanoseconds = end_nanoseconds - start_nanoseconds;
    double elapsed_microseconds = (double)elapsed_nanoseconds / 1000.0;

    printf("Factorial of %d is %lld\n", num, result);
    printf("Execution time: %.6f microseconds\n", elapsed_microseconds);

    return 0;
}

