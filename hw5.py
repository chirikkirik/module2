def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        line = []

        for j in range(m):
            line.append(value)

        matrix.append(line)

    return matrix

result = get_matrix(3, 4, 10)
print(result)

