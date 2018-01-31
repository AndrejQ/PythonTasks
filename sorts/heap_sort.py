def sort_tree(array):
    changed = True
    while changed:
        changed = False
        for i in range(len(array)):
            if 2 * i + 1 < len(array):
                if array[i] < array[2 * i + 1]:
                    array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
                    changed = True
            else:
                break
            if 2 * i + 2 < len(array):
                if array[i] < array[2 * i + 2]:
                    array[i], array[2 * i + 2] = array[2 * i + 2], array[i]
                    changed = True
            else:
                break
    return array


def heap_sort(array):
    # print(array)
    if len(array) == 1:
        return array
    array = sort_tree(array)
    array[0], array[-1] = array[-1], array[0]
    return heap_sort(array[:-1]) + [array[-1]]


def form(array):
    return " ".join(str(k) for k in array)


def my_sort(text):
    return form(heap_sort(text))


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
