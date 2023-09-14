// Says hello to the user
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Gets user input (name)
    string answer = get_string("What's your name? ");
    // Prints "Hello, <user input>!"
    printf("Hello, %s!\n", answer);
}