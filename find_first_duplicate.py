def find_first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen: