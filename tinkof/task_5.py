from numpy.random import randint


def delete(index_i, index_j, matrix):
    for i in range(M):
        matrix[i][index_j] = 0
    matrix[index_i] = [0] * N
    matrix[index_i][index_j] = 1
    return matrix


# lines = []
# while True:
#     line = input()
#     if line:
#         line = line.split(' ')
#         for i in range(len(line)):
#             line[i] = int(line[i])
#         lines.append(line)
#     else:
#         break

ppp = 3
lines = [[ppp, ppp]]
for i in range(ppp):
    lines.append([randint(2) for i in range(ppp)])
print('here')
print(lines)
N = lines[0][0]  # количество столбцов (скиллов)
M = lines[0][1]  # количество строк (спецов)
# [guy][skill]
matrix = []

for i in range(1, 1 + M):
    matrix.append(lines[i])

matrix = sorted(matrix, key=lambda x: sum(x))

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 1:
            # deleting
            matrix = delete(i, j, matrix)
            break

print(sum([sum(prof) for prof in matrix]))
