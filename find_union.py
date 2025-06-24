def find_union(arr1, arr2):
    result = []

    for item in arr1:
        if item not in result:
            result.append(item)

             for item in arr2:
        if item not in result:
            result.append(item)

            
    return result

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 6, 7, 8, 9]
print(find_union(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]