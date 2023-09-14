#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_digits(string s);
char rotate(string p, int k);

int main(int argc, string argv[])
{

    // Get single digit command-line argument
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Converting argv to an int
    int k = atoi(argv[1]);

    // Get user input for a plaintext
    string p = get_string("plaintext: ");

    // Print ciphertext
    printf("ciphertext: ");

    // Encrypts the plaintext
    char c = rotate(p, k);
    printf("%c\n", c);
    return 0;

}


// Check if key is a digit
bool only_digits(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

// Function that rotates the char according to the key
char rotate(string p, int k)
{
    char c;
    for (int i = 0; i < strlen(p); i++)
    {
        if islower(p[i])
        {
            printf("%c", ((p[i] - 'a') + k) % 26 + 'a');
        }
        else if isupper(p[i])
        {
            printf("%c", ((p[i] - 'A') + k) % 26 + 'A');
        }
        else
        {
            printf("%c", p[i]);
        }
    }

    printf("\n");
    return 0;
    return c;
}