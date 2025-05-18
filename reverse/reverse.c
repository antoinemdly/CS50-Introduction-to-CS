#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage :\n\n./reverse input.WAV output.WAV\n");
        return 1;
    }
    // Open input file for reading
    // TODO #2
    char *inptr = argv[1];
    char *outptr = argv[2];

    FILE *input = fopen(inptr, "r");
    if (input == NULL)
    {
        printf("Could not open %s.\n", inptr);
        return 4;
    }
    // Read header
    // TODO #3
    WAVHEADER Header;
    fread(&Header, sizeof(WAVHEADER), 1, input);
    // Use check_format to ensure WAV format
    // TODO #4
    check_format(Header);
    // Open output file for writing
    // TODO #5
    FILE *output = fopen(outptr, "w");
    if (output == NULL)
    {
        printf("Could not open %s.\n", outptr);
        return 4;
    }
    // Write header to file
    // TODO #6
    fwrite(&Header, 44, 1, output);
    // Use get_block_size to calculate size of block
    // TODO #7
    int block = get_block_size(Header);
    printf("%i\n", Header.numChannels);
    printf("%i\n", Header.bitsPerSample);
    // Write reversed audio to file
    // TODO #8

    fread(...,block, , input)

}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] != 'W' && header.format[1] != 'A' && header.format[2] != 'V' && header.format[3] != 'E')
    {
        printf("Unsupported file format.\n");
        return 5;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int k = header.numChannels * (header.bitsPerSample / 8)
    return k;
}