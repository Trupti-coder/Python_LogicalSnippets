def max_sub_array(arr):
    if len(arr) == 0:
        return 0
 max_sum = arr[0]
    current_sum = arr[0]