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