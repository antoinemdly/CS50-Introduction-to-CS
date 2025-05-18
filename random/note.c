#include <cs50.h>
#include <stdio.h>

void acc(int x, int y);

int i;
int j;
char dir;

int main (void)
{
    do
    {
        dir = get_char("Direction of the dash (q to quit): ");

        if (dir == 'w')
        {
            acc(0, 1);
        }
        else if (dir == 'a')
        {
            acc(-1, 0);
        }
        else if (dir == 's')
        {
            acc(0, -1);
        }
        else if (dir == 'd')
        {
            acc(1, 0);
        }

    } while (dir != 'q');

}

void acc(int x, int y)
{
    do
    {
        i = i + (x * 3);
        j = j + (y * 3);
        printf("x : %i and y : %i\n", i, j);
    }
     while (i != 12 && j != 12 && i != -12 && j != -12);

     do
     {
        i = i - (x * 1);
        j = j - (y * 1);
        printf("x : %i and y : %i\n", i, j);
     }
     while (i != 0 || j != 0);
}