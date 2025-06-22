def top_k_frequent(nums, k):
    # Step 1: Count frequencies

     frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

