lines = [[input()],input().split(' ')]
n = int(lines[0][0])
coords = sorted([int(lines[1][i]) - 1 for i in range(int(n / 2))])
odd = 0
even = 0
for i in range(int(n / 2)):
    odd += abs(coords[i] - 2 * i)
    even += abs(coords[i] - 2 * i - 1)
print(min(odd, even))
