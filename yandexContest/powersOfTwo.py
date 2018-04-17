file = open("input.txt", "r")
line = file.readline()
number = int(line)
print(len("{0:b}".format(1)))
file.close()
# number = 5
file = open("output.txt", "w")

if number == 0:
    file.write('0')
else:
    # размер двоичного числа соответствует количеству степеней двойки меньше заданного числа
    file.write(str(len("{0:b}".format(number))))
file.close()
