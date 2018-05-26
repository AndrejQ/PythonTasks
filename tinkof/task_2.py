line = input()
# i - first index for @
# j - last index for @
n = len(line)

for index in range(n):
    if line[index] == '@':
        i = index
        break

for index in range(n):
    if line[-1 - index] == '@':
        j = n - index - 1
        break

print(line[:i + 1] + line[i + 1:j][::-1] + line[j:])
