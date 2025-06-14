def array_to_object(arr):
    seen={}
    for num in arr:
        if num in seen:
            return num
        seen[num]=True
        return -1
