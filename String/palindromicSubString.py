def longest_palindrome(s):
    result = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]