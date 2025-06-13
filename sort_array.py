def sort_array(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:

                 # swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
array = [1, 4, 6, 8, 3, 4]
print(sort_array(array))  # Output: [1, 3, 4, 4, 6, 8]