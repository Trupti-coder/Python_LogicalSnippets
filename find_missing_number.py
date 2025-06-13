def find_missing_number(arr):
    n=len(arr)+1
    total_sum=n*(n+1)//2
    array_sum=sum(arr)
    missing_number=total_sum-array_sum
    return missing_number

# Example usage
arr = [1, 2, 4, 5, 6]
missing_number = find_missing_number(arr)
print(f"The missing number is: {missing_number}")



    