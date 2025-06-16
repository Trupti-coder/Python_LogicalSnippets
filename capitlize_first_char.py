def capitalize_first_char(arr):
    uppercased_arr = []

    
    for word in arr:
        if len(word) > 0:
            # Capitalize first character manually, leave the rest unchanged
            first_char = word[0].upper()
            capitalized_word = first_char + word[1:]
        else:
              capitalized_word = ""
        uppercased_arr.append(capitalized_word)

    return uppercased_arr

# Example usage
words = ["hello", "world", "this", "is", "javascript"]
capitalized_words = capitalize_first_char(words)
print(capitalized_words)  # Output: ['Hello', 'World', 'This', 'Is', 'Javascript']
