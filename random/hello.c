#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char input;

    do {
        input = get_char("type h to say hello\n");

        if (input != 'h')
            printf("This is not the right key\n");

    }   while (input !='h');

    printf("Hello!!!\n");

}