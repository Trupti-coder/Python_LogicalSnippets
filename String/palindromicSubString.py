def longest_palindrome(s):
    result = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
               if sub == sub[::-1] and len(sub) > len(result):
                result = sub
    return result

print(longest_palindrome("babad"))  # Output: "bab" or "aba"