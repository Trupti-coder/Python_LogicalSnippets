def find_major_element(arr):
    max_count = 0
    majority_element = None
     for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
