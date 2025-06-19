def group_by_condition(arr, condition):
    group1 = []
    group2 = []
    
    for item in arr:
        if condition(item):
            group1.append(item)
        else:
            group2.append(item)