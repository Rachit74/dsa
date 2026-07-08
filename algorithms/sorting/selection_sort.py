# finds the lowest value of the array and moves it to the front

test_cases = [
    [5, 2, 9, 1, 7, 3, 8, 6, 4],
    [12, 4, 15, 9, 1, 20, 7, 18, 3],
    [30, 25, 10, 40, 5, 35, 20, 15],
    [8, 3, 6, 1, 9, 2, 7, 5, 4],
    [50, 10, 70, 30, 90, 20, 60, 40, 80],
    [14, 2, 19, 7, 11, 5, 17, 9, 13],
    [100, 75, 50, 25, 0, 125, 150],
    [23, 45, 12, 67, 34, 89, 56, 78],
    [91, 27, 63, 14, 38, 72, 5, 49],
    [16, 8, 24, 4, 20, 12, 28, 2]
]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)

    print(arr)

for i in test_cases:
    selection_sort(i)