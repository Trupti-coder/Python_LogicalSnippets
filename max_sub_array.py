def max_sub_array(arr):
    if len(arr) == 0:
        return 0

    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]  # Start a new subarray
        else:
            current_sum += arr[i]  # Extend the current subarray

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(arr))  # Output: 6
