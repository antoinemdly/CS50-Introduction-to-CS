#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int n = get_int("int :");

    int m = n/2;

    printf("%i/2 = %i\n",n ,m);
}