def find_max_num(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num


# Example usage
arr = [1, 2, 3, 4, 5, 6]
print(find_max_num(arr))  # Output: 6