s = "abcdef"
print(''.join(s[i] for i in range(len(s)) if i % 2 != 0))  # Output: "bdf"
