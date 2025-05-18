#include <stdio.h>

int main (void)
{
    char c = '1';
    int num = c - '0';  // Explicit type casting

    printf("Character: %c\n", c);
    printf("Integer: %i\n", num);

}