#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // TODO

    if (strlen(input) == 1)
    {
        return input[0] - '0';
    }

    int DigitRemaining = strlen(input) - 1;
    int LastDigit = input[strlen(input) - 1] - '0' ;

    input[DigitRemaining] = '\0';
    string new = input;

    return LastDigit + 10 * convert(new);

}