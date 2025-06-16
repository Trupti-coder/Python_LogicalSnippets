def array_chunk(arr, k):
    result = []
    chunk = []
     for i in range(len(arr)):
        chunk.append(arr[i])
        if len(chunk) == k:
            result.append(chunk)
            chunk = []

             if len(chunk) > 0:
        result.append(chunk)
         return result
    
# Example usage
array = [1, 2, 3, 4, 5, 6, 6, 7, 88, 9, 90, 8, 5]
k = 2
result = array_chunk(array, k)
print(result)