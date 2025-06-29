from collections import Counter
s = "success"
counter = Counter(s)
print(counter.most_common(1))  # Output: [('s', 3)]
