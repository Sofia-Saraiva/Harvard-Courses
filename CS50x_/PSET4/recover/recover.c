#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open file
    FILE *input = fopen(argv[1], "r");

    // Check if it's valid
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // 512 bytes blocks
    unsigned char buffer[512];

    // Count images generated
    int count_image = 0;

    // File pointer for recovered images
    FILE *output = NULL;

    // char filename[8]
    char *filename = malloc(8 * sizeof(char));

    // Reads the 512 bytes blocks
    while (fread(buffer, sizeof(char), 512, input))
    {
        // Check if it's JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {

            if (count_image > 0)
            {
                fclose(output);
            }

            // Write the JPEG filenames
            sprintf(filename, "%03i.jpg", count_image);

            // Open output for writing
            output = fopen(filename, "w");

            // Count how many images are found
            count_image++;
        }


        if (output != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output);
        }
    }

    free(filename);
    fclose(input);
    fclose(output);
}