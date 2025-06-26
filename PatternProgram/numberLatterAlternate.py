n = 5
num = 1
char_code = 97
for i in range(n):
    line = ''
    for j in range(i + 1):
        if j % 2 == 0:
            line += str(num)
            num += 1
        else:
            line += chr(char_code)
            char_code += 1
    print(line)
