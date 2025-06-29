from collections import Counter
s = "programming"
duplicates = [k for k, v in Counter(s).items() if v > 1]
print(duplicates)  # Output: ['r', 'g', 'm']
