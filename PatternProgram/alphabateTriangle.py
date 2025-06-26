n = 5
char_code = 65
for i in range(1, n + 1):
    for j in range(i):
        print(chr(char_code), end=' ')
        char_code += 1
    print()
