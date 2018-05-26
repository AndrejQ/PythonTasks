import sys


def hierarchy(key, n):
    if key == 'X':
        return n
    elif relations[key] == 'X':
        return n + 1
    else:
        return hierarchy(relations[key], n + 1)


lines = []
while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == 'quit':
        break
    else:
        lines.append(line)

lines = []
while True:
    line = input()
    if line:
        line = line.split(' ')
        lines.append(line)
    else:
        break

n = int(lines[0][0])
relations = {}
for i in range(1, len(lines)):
    relations[lines[i][0]] = lines[i][1]

for name in sorted(list(relations.keys()) + ['X']):
    print(name, hierarchy(name, 0))
