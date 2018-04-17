def insert_in_output(output, number):
    output.reverse()
    for i in range(5):
        if number < output[i]:
            output.insert(i, number)
            output.pop()
            break
    output.reverse()
    return output


file = open("input.txt", "r")
lines = file.readlines()
sequence = ' '.join(lines)
sequence = sequence.split(' ')

for i in range(len(sequence)):
    sequence[i] = int(sequence[i])
file.close()

file = open("output.txt", "w")

output = []
for i in range(min(5, sequence[0])):
    output.append(sequence[i + 1])
    file.write(' '.join(map(str, sorted(output, reverse=True))))
    file.write('\n')

if sequence[0] <= 5:
    file.close()
else:
    output = sorted(output, reverse=True)
    for i in sequence[6:]:
        output = insert_in_output(output, i)
        file.write(' '.join(map(str, output)))
        file.write('\n')
    file.close()
