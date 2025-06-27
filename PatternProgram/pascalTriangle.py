def pascal_triangle(n):
    for i in range(n):
        val = 1
        print(' ' * (n - i), end='')
        for j in range(i + 1):