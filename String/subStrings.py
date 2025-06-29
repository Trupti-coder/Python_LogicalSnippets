s = "abc"
substrings = [s[i:j+1] for i in range(len(s)) for j in range(i, len(s))]
print(substrings)
