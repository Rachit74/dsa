"""
binary search works on sorted arrays to divide the array into half until the target is found
Best case: O(n)
Worst case: O(log n)
"""

def binary_search(arr, target, low=0, high=None):
    # calculate high index based on array length
    if high == None:
        high = len(arr) - 1
    
    middle_index = (low + high) // 2

    # check for empty array
    if low > high:
        return -1

    # check if middle equals target
    if target == arr[middle_index]:
        return middle_index
    
    # continue on left side of the array if the target is smaller than middle
    if target < arr[middle_index]:
        return binary_search(arr, target, low, middle_index - 1)

    # continue on the right side of the array if the target is larget than middle
    if target > arr[middle_index]:
        return binary_search(arr, target, middle_index + 1, high)

    # return -1 if element not found
    return -1


array = [5,10,15,20,25,30,35]

print(binary_search(array, 35))
