// Building a right-aligned pyramid
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get user input of the height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    // Rows of the pyramid
    for (int i = 0; i < n; i++)
    {
        // Columns of the pyramid
        for (int j = 0; j < n; j++)
        {
            // Print blankspaces and hashes
            if (i + j < n - 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }

        printf("\n");
    }
}