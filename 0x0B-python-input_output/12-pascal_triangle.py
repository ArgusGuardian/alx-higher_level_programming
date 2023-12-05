#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return [[]]
    tri = [[1],]
    for i in range(1, n):
        row = [1]
        for j in range(len(tri[i-1])):
            if j == len(tri[i-1]) - 1:
                row.append(1)
            else:
                row.append(tri[i-1][j] + tri[i-1][j+1])
        tri.append(row)

    return tri
