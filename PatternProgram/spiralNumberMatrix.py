def spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, left = 0, 0
    bottom, right = n - 1, n - 1
     while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
         for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1