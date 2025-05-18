#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float price = get_float("Price: ");
    float pourcent_off = get_float("Pourcentage off: ");
    float sale = price * (pourcent_off/100);
    printf("%.2f\n", sale);
}