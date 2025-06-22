def find_unique_elements(arr):
    xor = 0
    for num in arr:
        xor ^= num
 set_bit = 1
    while (xor & set_bit) == 0:
        set_bit <<= 1