#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Function declarations
void swap(int *a, int *b);
void selectionSort(int arr[], int placeholder, int arraySize);
void merge(int arr[], int l, int m, int h);
void mergeSort(int arr[], int Lb, int Ub);
int partition(int arr[], int lb, int ub, int partitionType);
void quickSortv1(int arr[], int lb, int ub);
int findMedian(int arr[], int lb, int ub);
void quickSortv2(int arr[], int lb, int ub);

// Function to get the current time in nanoseconds
long long getNanoSeconds() {

    struct timespec tp;
    clock_gettime(CLOCK_MONOTONIC, &tp);  // Get the current time in CLOCK_MONOTONIC clock
    return tp.tv_sec * 1e9 + tp.tv_nsec;  // Convert seconds to nanoseconds and add the nanoseconds component
}

int main(void) {

    int testValues[] = {100, 10000, 50000, 75000, 100000, 500000};
    int numTests = sizeof(testValues) / sizeof(testValues[0]);

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

    // Iterate over different test sizes
    for (int t = 0; t < numTests; t++) {

        int n = testValues[t];
        int a[n];
        double timeSpent = 0.0;
        clock_t begin, end;

        // Generate random numbers for the array
        for (int i = 0; i < n; i++)
            a[i] = rand() % n + 1;

        // Iterate over the sorting algorithms
        for (int i = 0; i < 4; i++) {

            int upperBound = (i == 0) ? n : n - 1;  // Set upper bound to n for selection sort
            int arrCopy[n];  // Create a copy of the original array
            memcpy(arrCopy, a, n * sizeof(int));

            long long startTime = getNanoSeconds();  // Record the start time in nanoseconds
            sortingAlgorithms[i](arrCopy, 0, upperBound);
            long long endTime = getNanoSeconds();  // Record the end time in nanoseconds
            double timeSpent = (double)(endTime - startTime) / 1e9;  // Calculate the time elapsed in seconds

            printf("Time elapsed for %s with n = %d: %f seconds\n", algorithmNames[i], n, timeSpent);

            // Check if the array is sorted correctly
            for (int j = 0; j < n - 1; j++) {

                if (arrCopy[j] > arrCopy[j + 1]) {

                    printf("%s did not sort the array correctly.\n", algorithmNames[i]);
                    return -1;
                }
            }
        }
    }

    printf("\n");
    return 0;
}

// Function definitions

// Function to swap to given integers
void swap(int *a, int *b) {

    // Swap the values of two integers
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selectionSort(int arr[], int placeholder, int arraySize) {

    // Iterate through the array
    for (int i = 0; i < arraySize - 1; i++) {

        int min = i;

        // Find the minimum element in the unsorted portion of the array
        for (int j = i + 1; j < arraySize; j++) {

            if (arr[min] > arr[j])
                min = j;
        }

        // Swap the minimum element with the current element
        if (min != i)
            swap(&arr[i], &arr[min]);
        
    }
}

void merge(int arr[], int l, int m, int h) {

    // Calculate the sizes of the two subarrays
    int n1 = m - l + 1;
    int n2 = h - m;

    // Create temporary arrays to hold the elements of the subarrays
    int *left = (int *)malloc(n1 * sizeof(int));
    int *right = (int *)malloc(n2 * sizeof(int));

    // Copy elements from the original array to the temporary array
    for (int i = 0; i < n1; i++)
        left[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        right[j] = arr[m + 1 + j];

    // Merge the two subarrays back into the original array
    int i = 0;
    int j = 0;
    int k = l;

    while (i < n1 && j < n2) {

        if (left[i] <= right[j]) {

            arr[k] = left[i];
            i++;

        } else {

            arr[k] = right[j];
            j++;
        }

        k++;
    }

    // Copy any remaining elements from the left subarray
    while (i < n1) {

        arr[k] = left[i];
        i++;
        k++;
    }

    // Copy any remaining elements from the right subarray
    while (j < n2) {

        arr[k] = right[j];
        j++;
        k++;
    }

    // Free the memory allocated for the temporary arrays
    free(left);
    free(right);
}

void mergeSort(int arr[], int Lb, int Ub) {

    // Check if the lower bound is less than or equal to the upper bound
    if (Lb <= Ub - 1) {
        // Check if the lower bound is equal to the upper bound
        if (Lb == Ub)
            return;

        // Calculate the middle index
        int m = Lb + (Ub - Lb) / 2;

        // Recursively sort the left and right subarrays
        mergeSort(arr, Lb, m);
        mergeSort(arr, m + 1, Ub);

        // Merge the sorted subarrays
        merge(arr, Lb, m, Ub);
    }
}

const int PARTITION_FIRST = 0;
const int PARTITION_MEDIAN = 1;

// Function to perform partitioning in Quick Sort
int partition(int arr[], int lb, int ub, int partitionType) {

    int pivot;

    // Determine the pivot based on the partition type
    if (partitionType == PARTITION_FIRST) {

        pivot = arr[lb]; // First element as pivot

    } else if (partitionType == PARTITION_MEDIAN) {

        int pivotIndex = findMedian(arr, lb, ub); // Find the median index
        pivot = arr[pivotIndex]; // Get the median element as pivot
        swap(&arr[lb], &arr[pivotIndex]); // Move the pivot element to the beginning
    }

    int i = lb + 1, j = ub;

    // Partition the array based on the pivot
    while (i <= j) {

        if (partitionType == 0) {
            // Partition for PARTITION_FIRST
            while (i <= j && arr[i] <= pivot)
                i++;
            while (i <= j && arr[j] > pivot)
                j--;
        } else if (partitionType == 1) {
            // Partition for PARTITION_MEDIAN
            while (i <= j && arr[i] < pivot)
                i++;
            while (i <= j && arr[j] >= pivot)
                j--;
        }

        if (i < j)
            swap(&arr[i], &arr[j]); // Swap elements if i and j have not crossed each other
    }

    swap(&arr[lb], &arr[j]); // Move the pivot to its final position

    return j; // Return the index of the pivot
}

// Function to find the median index of three elements
int findMedian(int arr[], int lb, int ub) {

    int mid = lb + (ub - lb) / 2;

    // Check the conditions to determine the median index
    if ((arr[lb] <= arr[mid] && arr[mid] <= arr[ub]) || (arr[ub] <= arr[mid] && arr[mid] <= arr[lb])) {

        return mid; // Mid index is the median

    } else if ((arr[mid] <= arr[lb] && arr[lb] <= arr[ub]) || (arr[ub] <= arr[lb] && arr[lb] <= arr[mid])) {

        return lb; // lb index is the median

    } else {

        return ub; // ub index is the median
    }
}

// Quick Sort using the first element as the pivot
void quickSortv1(int arr[], int lb, int ub) {

    if (lb < ub) {

        int pivotIndex = partition(arr, lb, ub, PARTITION_FIRST); // Get the pivot index using the first element as the pivot
        quickSortv1(arr, lb, pivotIndex - 1); // Sort the left subarray
        quickSortv1(arr, pivotIndex + 1, ub); // Sort the right subarray
    }
}

// Quick Sort using the median element as the pivot
void quickSortv2(int arr[], int lb, int ub) {

    if (lb < ub) {

        int pivotIndex = partition(arr, lb, ub, PARTITION_MEDIAN); // Get the pivot index using the median element as the pivot
        quickSortv2(arr, lb, pivotIndex - 1); // Sort the left subarray
        quickSortv2(arr, pivotIndex + 1, ub); // Sort the right subarray
    }
}
