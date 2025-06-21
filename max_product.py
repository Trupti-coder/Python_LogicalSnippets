def max_product(arr):
 max_prod = float('-inf')
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_prod:
                max_prod = product
    return max_prod
# Example usage
arr = [1, 3, 4, 5, 6, 7, 8, 9]
print(max_product(arr))  # Output: 72