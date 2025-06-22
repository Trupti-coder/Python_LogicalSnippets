def find_pairs(arr, target):
    pairs = []
     for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append([arr[i], arr[j]])
    return pairs
# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
target = 18
print(find_pairs(arr, target))  # Output: []

