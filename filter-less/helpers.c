#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // for each row
    for (int i = 0; i < height; i++)
    {
        //for each pixel in the row
        for (int j = 0; j < width; j++)
        {
            float avg = (image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0 ;
            image[i][j].rgbtBlue = round(avg);
            image[i][j].rgbtRed = round(avg);
            image[i][j].rgbtGreen = round(avg);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // for each row
    for (int i = 0; i < height; i++)
    {
        //for each pixel in the row
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            float sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
            float sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
            float sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;

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


            image[i][j].rgbtBlue = round(sepiaBlue);
            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtGreen = round(sepiaGreen);
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int half = width/2;
    // for each row
    for (int i = 0; i < height; i++)
    {
        //for each pixel in the row
        for (int j = 0; j < half; j++)
        {
            RGBTRIPLE temp;
            temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    // for each row
    for (int i = 0; i < height; i++)
    {
        //for each pixel in the row
        for (int j = 0; j < width; j++)
        {
            float blurRed = 0;
            float blurGreen = 0;
            float blurBlue = 0;
            int count = 0;
            // for that pixel take 3 row
            for (int m = i - 1; m <= i + 1; m++)
            {
                // for that row take 3 colomn
                for (int n = j - 1; n <= j + 1; n++)
                {
                    if (m >= 0 && m < height && n >= 0 && n < width)
                    {
                        blurRed = blurRed + image[m][n].rgbtRed;
                        blurGreen = blurGreen + image[m][n].rgbtGreen;
                        blurBlue = blurBlue + image[m][n].rgbtBlue;
                        count++;
                    }
                }
            }

            copy[i][j].rgbtRed = round(blurRed/count);
            copy[i][j].rgbtGreen = round(blurGreen/count);
            copy[i][j].rgbtBlue = round(blurBlue/count);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copy[i][j].rgbtRed;
            image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
        }
    }

    return;
}
