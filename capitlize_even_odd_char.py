def capitlize_even_odd_char(char):
    capitlized_arr=[]

    for word in arr:
        capitalized_word = ''
        for i in range(len(word)):
            char = word[i]
            if i % 2 == 0:

                capitalized_word += char.upper()
            else:
                capitalized_word += char.lower()
        capitalized_arr.append(capitalized_word)

    return capitalized_arr

# Example usage
arr = ["hello", "world", "this", "is", "javascript"]
print(capitalize_even_odd_char(arr))
# Output: ['HeLlO', 'WoRlD', 'ThIs', 'Is', 'JaVaScRiPt']


