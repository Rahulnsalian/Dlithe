#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s[] = "abc"; // Corrected declaration of s as a character array
    int a[] = {3, 5, 9}; // Corrected initialization of integer array a
    printf("%s\n", s); // Using %s to print the string s
    int sum = 0;
    int i;

    for (i = 0; i <= 2; i++)
    {
        sum = sum + a[i];
    }
    for (i = 0; i <= 2; i++)
    {
        int shifted_char = s[i] + sum;
        if (shifted_char > 'z')
        {
            shifted_char = shifted_char - 26;
        }
        s[i] = shifted_char;
        sum = sum - a[i];
    }
    printf("%s\n", s);

    return 0; // Adding a return statement at the end of the main function
}
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s[] = "abc"; // Corrected declaration of s as a character array
    int a[] = {3, 5, 9}; // Corrected initialization of integer array a
    printf("%s\n", s); // Using %s to print the string s
    int sum = 0;
    int i;

    for (i = 0; i <= 2; i++)
    {
        sum = sum + a[i];
    }
    for (i = 0; i <= 2; i++)
    {
        int shifted_char = s[i] + sum;
        if (shifted_char > 'z')
        {
            shifted_char = shifted_char - 26;
        }
        s[i] = shifted_char;
        sum = sum - a[i];
    }
    printf("%s\n", s);

    return 0; // Adding a return statement at the end of the main function
}