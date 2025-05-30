#include <cs50.h>
#include <stdio.h>

#define NUM_CITIES 10

typedef struct
{
    string city;
    int temp;
} avg_temp;

avg_temp temps[NUM_CITIES];

void sort_cities(int low, int high);
int partition(int low, int high);
void swap(int i, int j);

int main(void)
{
    temps[0].city = "Austin";
    temps[0].temp = 97;

    temps[1].city = "Boston";
    temps[1].temp = 82;

    temps[2].city = "Chicago";
    temps[2].temp = 85;

    temps[3].city = "Denver";
    temps[3].temp = 90;

    temps[4].city = "Las Vegas";
    temps[4].temp = 105;

    temps[5].city = "Los Angeles";
    temps[5].temp = 82;

    temps[6].city = "Miami";
    temps[6].temp = 97;

    temps[7].city = "New York";
    temps[7].temp = 85;

    temps[8].city = "Phoenix";
    temps[8].temp = 107;

    temps[9].city = "San Francisco";
    temps[9].temp = 66;

    sort_cities(0, NUM_CITIES - 1);

    printf("\nAverage July Temperatures by City\n\n");

    for (int i = 0; i < NUM_CITIES; i++)
    {
        printf("%s: %i\n", temps[i].city, temps[i].temp);
    }
}

void sort_cities(int low, int high)
{
    if (low < high)
    {
        int pi = partition(low, high);

        sort_cities(low, pi - 1);
        sort_cities(pi + 1, high);
    }
}

int partition(int low, int high)
{
    int pivot = temps[high].temp;
    int i = low - 1;

    for (int j = low; j <= high - 1; j++)
    {
        if (temps[j].temp >= pivot)
        {
            i++;
            swap(i, j);
        }
    }

    swap(i + 1, high);
    return i + 1;
}

void swap(int i, int j)
{
    avg_temp temp = temps[i];
    temps[i] = temps[j];
    temps[j] = temp;
}
