def intersection_of_array(arr1, arr2):
    result = []
    arr2_copy = arr2.copy()  # To avoid modifying the original arr2
     for item1 in arr1:
        for i in range(len(arr2_copy)):
            if item1 == arr2_copy[i]:
                result.append(item1)
                arr2_copy[i] = None  # Mark as used
                break
  return result

# Example usage
arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 4, 5]
print(intersection_of_array(arr1, arr2))  # Output: [2, 3, 4]