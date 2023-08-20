#include <stdio.h>
#define LEN_INPUT 10

int main(void) {
    char s1[LEN_INPUT];
    scanf("%s", s1);
    
    int i = 0;
    while (s1[i]) {  
        if (islower(s1[i])) {
            s1[i] = toupper(s1[i]);
        } else if (isupper(s1[i])) {
            s1[i] = tolower(s1[i]);
        }
        i++;
    }
    printf("%s", s1);
    return 0;
}
