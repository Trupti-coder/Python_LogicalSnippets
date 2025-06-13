def rotate_array(array, k):
    n = len(array)
    k = k % n  # handle if k > n
    result = [0] * n

    for i in range(n):
          
          result[(i + k) % n] = array[i]

    # copy back to original array if needed, or just return result
    return result

    # # copy back to original array if needed, or just return result
    # return result

    # Example usage
array = [1, 2, 3, 4, 5]
rotated = rotate_array(array, 2)
print(rotated)  # Output: [4, 5, 1, 2, 3]