def rotate_array(array, k):
    n = len(array)
    k = k % n  # handle if k > n
    result = [0] * n