#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    char *plates[8];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    for (int i = 0; i < 8; i++)
    {
        fread(buffer,1,7,infile);

        buffer[6] = '\0';
        plates[i] = buffer;

        printf("%s\n", plates[i]);
    }

    fclose(infile);

    /*
    while (fread(buffer, 1, 7, infile) == 7)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // Save plate number in array
        plates[idx] = buffer;
        idx++;
    }
    */
    /*
    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);
    }
    */
}
