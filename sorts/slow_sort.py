def form(array):
    return " ".join(str(k) for k in array)


def my_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1):
            if array[i - j] > array[i - j + 1]:
                array[i - j], array[i - j + 1] = array[i - j + 1], array[i - j]
    return form(array)


# lines = []
# while True:
#     line = input()
#     if line:
#         lines.append(line)
#     else:
#         break
# text = ' '.join(lines)
# text = text.split(' ')
# for i in range(len(text)):
#     text[i] = int(text[i])
file = open("input.txt", "r")
lines = file.readlines()
text = ' '.join(lines)
text = text.split(' ')
for i in range(len(text)):
    text[i] = int(text[i])
file.close()
file = open("output.txt", "w")
file.write(my_sort(text))
file.close()
print(my_sort(text))
