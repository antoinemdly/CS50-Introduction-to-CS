#include <cs50.h>
#include <stdio.h>



int main (void)
{
    int i = 0;

    do
    {
        i = i + 3;
        printf("speed : %i\n", i);
    }
     while (i < 12);

     do
     {
        i = i - 1;
        printf("speed : %i\n", i);
     }
     while (i > 0);
}