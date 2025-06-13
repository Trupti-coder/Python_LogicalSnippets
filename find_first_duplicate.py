def find_first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
                 return num
        seen.add(num)
    return -1  # no duplicates

# Example usage
arr = [1, 2, 3, 4, 5, 4]
print(find_first_duplicate(arr))  # Output: 4