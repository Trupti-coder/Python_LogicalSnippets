def reverse_array(array):
    start = 0
    end = len(array) - 1
    while start < end:
        # swap elements at start and end
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    return array


# Example usage
original_array = [1, 2, 3, 4, 5, 6]
new_array = reverse_array(original_array)
print(new_array)  # Output: [6, 5, 4, 3, 2, 1]