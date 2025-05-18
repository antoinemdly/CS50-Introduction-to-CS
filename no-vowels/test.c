#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *s = "HI!";
    printf("%s\n", &s[1]);
    printf("%c\n", s[1]);
    printf("%p\n", &s[0]);
    printf("%c\n", *s + 1);
}
