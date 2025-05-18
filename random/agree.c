#include <stdio.h>
#include <cs50.h>

int main(void)
{

    char response;

    response = get_char("Do you agree ? y or n\n");

    while (response != 'y' && response != 'n')
        {


        printf("Please enter a valid answer.\n");


        response = get_char("Do you agree ? y or n\n");

        }


        if (response == 'n')
        {
            printf("not agreed\n");
        }

        else
        {
            printf("agreed.\n");
        }
}