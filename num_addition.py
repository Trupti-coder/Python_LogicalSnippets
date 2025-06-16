def num_addition():
    input_str = "a2b4c6d3"
    total = 0
    i = 0
     while i < len(input_str):
        if input_str[i].isdigit():
            num = 0

             while i < len(input_str) and input_str[i].isdigit():
                num = num * 10 + int(input_str[i])
                i += 1
            total += num