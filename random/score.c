#include <cs50.h>
#include <stdio.h>



int main (void)
{
    int n = get_int("Number of scores: ");

    int score[n];
    float sum;

    for (int i = 0 ; i<n ; i++)
    {
        score[i] = get_int("Score %i: ", i+1);
        sum = sum + score[i];
    }
    float avg = sum / n;

    printf("Average: %.1f\n", avg);


}