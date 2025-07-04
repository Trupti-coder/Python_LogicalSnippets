s = "John Ronald Reuel Tolkien"
abbrev = '.'.join(word[0].upper() for word in s.split()) + '.'
print(abbrev)  # Output: J.R.R.T.
