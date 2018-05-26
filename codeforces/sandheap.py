line = input()
line = line.split(' ')
n = int(line[0])
h = int(line[1])
n_bord = (h - 1) * h / 2
if n_bord >= n:
    # counter = 1
    counter = int((-1 + (1 + 8 * n) ** 0.5) / 2)
    while True:
        if counter * (counter + 1) / 2 >= n:
            print(counter)
            break
        counter += 1
else:
    counter = 2 * (h - 1) + 1
    counter = int((-1 + (1 + 4 * (n + n_bord)) ** 0.5)) - 1
    while True:
        if counter % 2 == 0:  # 2 4 6 8
            if counter * (counter + 2) / 4 - n_bord >= n:
                print(counter - h + 1)
                break
        else:  # 1 3 5 7
            if ((counter + 1) / 2) ** 2 - n_bord >= n:
                print(counter - h + 1)
                break
        counter += 1
