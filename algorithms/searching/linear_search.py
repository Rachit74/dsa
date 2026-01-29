"""
simple squential searching algorithm where we check each element in the list one by one in order
Time Complexity:
Best case: O(1) -> target is first element
Worst case: O(n) -> target is the last element
Average case: O(n/2)
"""

array = [5,3,6,9,4,1,7]

def linear_search(arr, target):
    # loop over the array and find target
    for i, val in enumerate(arr):
        if val == target:
            return i
        
    return -1

print(linear_search(arr=array, target=9))