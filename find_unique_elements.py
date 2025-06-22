def find_unique_elements(arr):
    xor = 0
    for num in arr:
        xor ^= num
 set_bit = 1
    while (xor & set_bit) == 0:
        set_bit <<= 1
         num1 = 0
    num2 = 0
    for num in arr:
        if num & set_bit:
            num1 ^= num
             else:
            num2 ^= num

    return [num1, num2]