#ifndef SORTING_H
#define SORTING_H

void swap(int *a, int *b);
void selectionSort(int arr[], int placeholder, int arraySize);
void merge(int arr[], int l, int m, int h);
void mergeSort(int arr[], int Lb, int Ub);
void quickSortv1(int arr[], int lb, int ub);
void quickSortv2(int arr[], int lb, int ub);

#endif
