#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int div =10;
    while(1)
    {
        answer += (n % div);
        
        if((n/div) == 0)
        {
            break;
        }
        
        n /= div;
    }
    return answer;
}