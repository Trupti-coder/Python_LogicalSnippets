def find_second_smallest(arr):
    if len(arr) < 2:
        return False

    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return None if second_smallest == float('inf') else second_smallest

# Example usage
numbers = [5, 3, 8, 1, 2]
result = find_second_smallest(numbers)
print("Second smallest:", result)  # Output: Second smallest: 2
