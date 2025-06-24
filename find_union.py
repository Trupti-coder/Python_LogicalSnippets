def find_union(arr1, arr2):
    result = []

    for item in arr1:
        if item not in result:
            result.append(item)