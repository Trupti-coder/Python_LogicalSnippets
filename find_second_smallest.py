def find_second_smallest(arr):
    if len(arr) < 2:
        return False
    smallest = float('inf')
    second_smallest = float('inf')
     for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num