#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "sorting.h"

#define n 10000

int main(void) {
    int a[n];
    double timeSpent = 0.0;
    clock_t begin, end;

    // Generate random numbers
    for (int i = 0; i < n; i++)
        a[i] = rand() % n + 1;

    // Define an array of sorting algorithm functions
    void (*sortingAlgorithms[])(int[], int, int) = {

        selectionSort,
        mergeSort,
        quickSortv1,
        quickSortv2
    };

    // Define an array of sorting algorithm names
    const char* algorithmNames[] = {

        "Selection Sort",
        "Merge Sort",
        "Quick Sort v1",
        "Quick Sort v2"
    };

    // Iterate over the sorting algorithms
    for (int i = 0; i < 4; i++) {

        int upperBound = (i == 0) ? n : n - 1;  // Set upper bound to n for selection sort
        int arrCopy[n];  // Create a copy of the original array
        memcpy(arrCopy, a, n * sizeof(int));

        begin = clock();
        sortingAlgorithms[i](arrCopy, 0, upperBound);
        end = clock();
        timeSpent = (double)(end - begin) / CLOCKS_PER_SEC;

        printf("Time elapsed for %s: %f seconds\n", algorithmNames[i], timeSpent);

        // Check if array is sorted
        for (int j = 0; j < n - 1; j++) {
            if (arrCopy[j] > arrCopy[j + 1]) {
                printf("%s did not sort the array correctly.\n", algorithmNames[i]);
                return -1;
            }
        }
    }

    return 0;
}
