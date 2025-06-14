def array_to_object(arr):
    seen={}
    for num in arr:
        if num in seen:
            return num
        seen[num]=True
        return -1
    
# Example usage
arr = [1, 2, 3, 4, 5, 4]
print(array_to_object(arr))  # Output: 4
