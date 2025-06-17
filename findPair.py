def find_pairs(arr, target):
    pairs = []
     for i in range(len(arr)):
        for j in range(i + 1, len(arr)):