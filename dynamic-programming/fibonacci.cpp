#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int fibo(int n);
int fiboM(int n, int memo[]);

int SIZE = 100;

int main(){

    int memo[SIZE];

    for (int i = 0; i < SIZE; i++){
        memo[i] = -1;
    }

    cout<< fiboM(7, memo) << "\n";

    return 0;
}

// Recursive
int fibo(int n) {
    if(n == 0){
        return 0;
    }

    if(n == 1){
        return 1;
    }

    return fibo(n - 1) + fibo(n - 2);
}

// Memoized 

// AI Review

// No Negative Input Handling
// Memory Management: vector or unordered_map for safer memory management & dynamic sizing
// Returning -1 for n >= SIZE is ambiguous, use exceptions, or error-handling mechanism
// Avoid global variables
// Fixed array size

int fiboM(int n, int memo[]) {

    if(n >= SIZE){
        return -1;
    }

    if(memo[n] != -1){
        return memo[n];
    }

    if(n == 0){
        return 0;
    }

    if(n == 1){
        return 1;
    }

    memo[n] = fiboM(n - 1, memo) + fiboM(n - 2, memo);
    return memo[n];
}

// Next Time

// Try Iterative Approach next time
// Create fixed version