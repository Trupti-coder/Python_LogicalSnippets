def find_major_element(arr):
    max_count = 0
    majority_element = None

    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count > max_count:
            max_count = count
            majority_element = arr[i]

    return majority_element

# Example usage
arr = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9, 9, 9]
print(find_major_element(arr))  # Output: 9
