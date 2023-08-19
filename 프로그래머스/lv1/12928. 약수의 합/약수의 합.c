#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
     int answer = 0;

    if (n == 1)
        return 1; // 1의 약수는 자기 자신만

    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            answer += i;
        }
    }

    return answer + n;
}