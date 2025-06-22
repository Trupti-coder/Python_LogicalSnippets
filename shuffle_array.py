import random

def shuffle_array(arr):
    for i in range(len(arr) - 1, 0, -1):
        random_index = random.randint(0, i)
        arr[i], arr[random_index] = arr[random_index], arr[i]  # Swap elements
    return arr