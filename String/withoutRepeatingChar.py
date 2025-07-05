s = "this challenge is interesting"
words = s.split()
max_len = 0
for word in words:
       if len(set(word)) == len(word):
        max_len = max(max_len, len(word))
print(max_len)  # Output: 11 (interesting)