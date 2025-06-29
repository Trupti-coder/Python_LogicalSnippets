import string
s = "Hello, world!"
s_clean = "".join(c for c in s if c not in string.punctuation)
print(s_clean)  # Output: "Hello world"
