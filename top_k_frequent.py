def top_k_frequent(nums, k):
    # Step 1: Count frequencies

     frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

         # Step 2: Create buckets
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in frequency_map.items():
        buckets[freq].append(num)



