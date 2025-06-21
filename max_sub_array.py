def max_sub_array(arr):
    if len(arr) == 0:
        return 0
 max_sum = arr[0]
    current_sum = arr[0]
 for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]  # Start a new subarray
        else: