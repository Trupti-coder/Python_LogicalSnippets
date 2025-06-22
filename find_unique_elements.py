def find_unique_elements(arr):
    xor = 0
    for num in arr:
        xor ^= num
