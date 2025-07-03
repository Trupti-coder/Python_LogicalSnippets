def is_substring(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return True
    return False

print(is_substring("hello", "ell"))  # Output: True
