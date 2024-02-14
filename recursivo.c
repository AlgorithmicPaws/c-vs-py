#include <stdio.h>
#include <sys/time.h>

long long factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int num;
    printf("Enter a number to calculate its factorial: ");
    scanf("%d", &num);

    struct timeval start_time, end_time;
    gettimeofday(&start_time, NULL); // Get start time

    long long result = factorial(num);

    gettimeofday(&end_time, NULL); // Get end time

    // Calculate elapsed time in microseconds
    long long start_microseconds = start_time.tv_sec * 1000000 + start_time.tv_usec;
    long long end_microseconds = end_time.tv_sec * 1000000 + end_time.tv_usec;
    long long elapsed_microseconds = end_microseconds - start_microseconds;

    printf("Factorial of %d is %lld\n", num, result);
    printf("Execution time: %lld microseconds\n", elapsed_microseconds);

    return 0;
}
 