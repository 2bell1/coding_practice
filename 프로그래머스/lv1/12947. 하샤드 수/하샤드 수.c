#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    int sum=0;
    int temp = x;
    while(1)
    {
        sum += (x % 10);
        if((x / 10) == 0)
            break;
        else
            x /= 10;
    }
    
    if((temp % sum) == 0)
        answer = true;
    else
        answer = false;
    
    return answer;
}