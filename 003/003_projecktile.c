/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <stdio.h>

int main(void){
    // unsigned long long int limit = 600851475143, cap = limit;
    unsigned long long int limit = 102, cap = limit;

    unsigned long int prime;
    unsigned long long int i;
    for (i = 1; i < cap; i++){
        if (limit % i == 0){
            cap = limit/i;
            unsigned long int n;
            for (n = 1; n <= i+1; n++){
                if (n > 1){
                    if (i == n){
                        prime = i;
                        break;
                    }
                    else if (i % n == 0){
                        break;
                    }
                }
            }
        }
    }
    printf("%lld\n", prime);
    return 0;
}