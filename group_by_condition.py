def group_by_condition(arr, condition):
    group1 = []
    group2 = []
    
    for item in arr:
        if condition(item):
            group1.append(item)
        else:
            group2.append(item)
           
    return [group1, group2]
# Example usage: Group even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grouped_numbers = group_by_condition(numbers, lambda num: num % 2 == 0)

print(grouped_numbers)  # Output: [[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]]