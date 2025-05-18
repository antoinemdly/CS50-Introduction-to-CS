#include <stdio.h>
#include <cs50.h>
/*
int main (void)
{
    int n = get_int("n : ");
    int sum = n;

    for (int i = 1; i < n; i++)
    {
        sum = sum * (n-i);
    }

    printf("!n = %i\n", sum);
}
*/
int fact (int n);

int main (void)
{
    int n = get_int("n : ");
    printf("%i\n", fact(n));
}

int fact (int n)
{
    if (n == 1)
    {
       return 1;
    }

    int sum = n * fact(n-1);

    return sum;
}