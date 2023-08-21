#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
   long long answer = 0;
    
    if (a == b)
        return a;

    int start = (a < b) ? a : b;
    int end = (a > b) ? a : b;
    
    for (int i = start; i <= end; i++) {
        answer += i;
    }
    
    return answer;
}