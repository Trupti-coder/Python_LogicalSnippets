import string
s = "The quick brown fox jumps over the lazy dog"
print(set(string.ascii_lowercase).issubset(set(s.lower())))  # Output: True
