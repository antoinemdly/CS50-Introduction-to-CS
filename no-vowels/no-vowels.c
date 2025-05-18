// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string argv);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("not correct form\n");
        return 1;
    }

    string final = replace(argv[1]);
    printf("%s\n", final);
    return 0;
}

string replace(string input)
{
    for (int i = 0; i < strlen(input); i++)
    {
        switch (input[i])
        {
            case 'a':
                input[i] = '6';
                break;

            case 'e':
                input[i] = '3';
                break;

            case 'i':
                input[i] = '1';
                break;

            case 'o':
                input[i] = '0';
                break;

            default:

                break;
        }
    }
    return input;
}
