def find_union(arr1, arr2):
    result = []

    for item in arr1:
        if item not in result:
            result.append(item)

             for item in arr2:
        if item not in result:
            result.append(item)