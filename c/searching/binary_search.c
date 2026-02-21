#include <stdio.h>

int binary_search(int *arr, int target, int low, int high) {
    int mid = (low + high) / 2;

    if (low > high) {
        return -1;
    }

    // check if mid is the targert
    if (arr[mid] == target) {
        return mid;
    } else if (arr[mid] < target)
    {
        return binary_search(arr, target, mid + 1, high);
    } else if (arr[mid] > target)
    {
        return binary_search(arr, target, low, mid - 1);
    } else {
        return -1;
    }
        
}

int main() {
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    int len = sizeof(arr)/sizeof(int);

    int index = binary_search(arr, 7, 0, len-1);
    printf("Target Index is: %d\n", index);
}