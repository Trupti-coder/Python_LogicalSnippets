def one_edit_apart(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    i = j = edits = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edits == 1:
                return False
            edits += 1
            if len(s1) == len(s2):
                i += 1
        else:
            i += 1
        j += 1
    return True

print(one_edit_apart("pale", "ple"))  # Output: True
