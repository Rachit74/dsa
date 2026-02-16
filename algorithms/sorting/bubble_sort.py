

test_cases = [
    
]


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            # compare n swap
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        
    print(arr)
                


bubble_sort(arr1)
bubble_sort(arr2)
bubble_sort(arr3)
bubble_sort(arr4)
bubble_sort(arr5)
