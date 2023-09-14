#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Rows
    for (int i = 0; i < height; i++)
    {
        // Columns
        for (int j = 0; j < width; j++)
        {
            // Converting pixels to floats
            float Red = image[i][j].rgbtRed;
            float Green = image[i][j].rgbtGreen;
            float Blue = image[i][j].rgbtBlue;

            // Formula
            int average = round((Red + Green + Blue) / 3);

            // Updating the pixel values
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Rows
    for (int i = 0; i < height; i++)
    {
        // Columns
        for (int j = 0; j < width; j++)
        {
            // Converting pixels to float
            float originalRed = image[i][j].rgbtRed;
            float originalGreen = image[i][j].rgbtGreen;
            float originalBlue = image[i][j].rgbtBlue;

            // Formula
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            // If sepiaRed, sepiaBlue or sepiaGreen exceed 255, lock pixel value to 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // Updating pixel values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Rows
    for (int i = 0; i < height; i++)
    {
        // Columns
        for (int j = 0; j < width / 2; j++)
        {
            // Rearranging the pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    // Rows
    for (int i = 0; i < height; i++)
    {
        // Columns
        for (int j = 0; j < width / 2; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    // Rows
    for (int i = 0; i < height; i++)
    {
        // Columns
        for (int j = 0; j < width; j++)
        {
            int totalRed, totalBlue, totalGreen;
            totalRed = totalBlue = totalGreen = 0;
            float counter = 0.00;

            // Get pixels near it
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int nX = i + x;
                    int nY = j + y;

                    // Check if pixel near it is valid
                    if (nX < 0 || nX > (height - 1) || nY < 0 || nY > (width - 1))
                    {
                        continue;
                    }

                    // Get the image value
                    totalRed += image[nX][nY].rgbtRed;
                    totalGreen += image[nX][nY].rgbtGreen;
                    totalBlue += image[nX][nY].rgbtBlue;

                    counter++;

                    // Average of pixels near it
                    temp[i][j].rgbtRed = round(totalRed / counter);
                    temp[i][j].rgbtGreen = round(totalGreen / counter);
                    temp[i][j].rgbtBlue = round(totalBlue / counter);
                }
            }
        }
    }

    // Paste the temporary blue into original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}
