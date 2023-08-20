#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int div = 1;
    int remainder = 0;
    while(1)
    {
        remainder = n % div;
        if(remainder == 1)
        {
            answer = div;
            break;
        }
        div++;
    }
    return answer;
}