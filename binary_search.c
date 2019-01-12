#include <stdio.h>  

int binary_search(int[], int, int);

int main()
{
    int list[] = {1, 2, 3, 4, 5, 7};
    int lenght = 6;

    printf("%d\n", binary_search(list, 7, lenght));
    printf("%d\n", binary_search(list, -1, lenght));

    return 0;

}

int binary_search(int list[], int object, int lenght)
{
    int low = 0;
    int high = lenght;
    
    while(low <= high)
    {
        int middle;
        if ((low + high) % 2 == 0)
            middle = (low + high) / 2;
        else
            middle = (low + high) / 2 + 1;
        int guess = list[middle];
        
        if (guess == object)
        {
            return middle;
        }
        else if (guess > object)
        {
            high = middle - 1;
        }
        else
        {
            low = middle + 1;
        }
    }
        return -1;
}