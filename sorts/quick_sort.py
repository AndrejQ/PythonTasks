def quick_sort(array):
    left = []
    middle = []
    right = []
    if len(array) <= 1:
        return array
    for num in array:
        if num < array[0]:
            left.append(num)
        elif num > array[0]:
            right.append(num)
        else:
            middle.append(num)
    return quick_sort(left) + middle + quick_sort(right)


def form(array):
    return " ".join(str(k) for k in array)


def my_sort(text):
    return form(quick_sort(text))


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
