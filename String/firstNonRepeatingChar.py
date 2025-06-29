from collections import Counter
s = "aabbccde"
counter = Counter(s)
for ch in s:
    if counter[ch] == 1:
        print(ch)  # Output: d
        break