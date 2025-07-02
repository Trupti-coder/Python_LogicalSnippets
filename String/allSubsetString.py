s = "abc"
subsets = []
for i in range(2 ** len(s)):
    subset = ''.join(s[j] for j in range(len(s)) if (i >> j) & 1)
    subsets.append(subset)
print(subsets)