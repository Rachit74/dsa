"""
create a hashmap for every value in the array, store the element as key and index as value
O(1) time complexity
"""

def hash_search(arr, target):
    lookup = {}

    for i, value in enumerate(arr):
        lookup[value] = i
    
    index = lookup.get(target, -1)

    return index


array = [23,45,12,67,98,35,66,21]

print(hash_search(array, 67))