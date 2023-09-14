// Calculates the approximate grade level needed to comprehend a text
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{

    // Get text input from the user
    string text = get_string("Text: ");

    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Calculate average of letters and sentences
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    // Calculate the grade using Coleman-Liau index
    float calculation = (0.0588 * L - 0.296 * S - 15.8);
    int index = round(calculation);

    // Prints the grade needed to comprehend a text
    if (index >= 16)
    {
        printf("Grade 16+\n");
        return 0;
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }
    else
    {
        printf("Grade %i\n", index);
        return 0;
    }

}


int count_letters(string text)
{

    // Function to count letters
    int letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;

}

int count_words(string text)
{

    // Function to count words
    int words = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            words++;
        }
    }
    return words;

}

int count_sentences(string text)
{

    // Function to count sentences
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }
    return sentences;

}