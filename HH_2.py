import copy
import sys

/* 
Предположим, в один прекрасный день вы оказались на острове прямоугольный формы.
Ландшафт этого острова можно описать с помощью целочисленной матрицы размером MxN,
каждый элемент которой задаёт высоту соответствующей области острова над уровнем моря.
В сезон дождей остров полностью заливает водой и в низинах скапливается вода.
Низиной будем считать такую область острова, клетки которой граничат с клетками,
большими по высоте. При этом диагональные соседи не учитываются, а уровень моря принимается за 0.

На вход функции подается массив массивов, на выходе ожиается int - значения общего объёма воды,
скапливающейся на острове после сезона дождей для каждого из входных примеров Ограничения:
Размер острова N и M — целые числа в диапазоне [1, 50]
Высоты на острове могут принимать значения из диапазона [1, 1000]
*/


max_value = lambda x: max([max(i) for i in x])
min_value = lambda x: min([min(i) for i in x])

def printt(listt):
    for i in listt:
        print(i)
    print('=============================')

def fill(strk, stlb):
    global isla

    isla[strk][stlb] = 4

    if strk < len(isla) -1:
        if isla[strk + 1][stlb] == 0:
            fill(strk + 1, stlb)

    if strk > 0:
        if isla[strk - 1][stlb] == 0:
            fill(strk - 1, stlb)

    if stlb < len(isla[0]) - 1:
        if isla[strk][stlb + 1] == 0:
            fill(strk, stlb + 1)

    if stlb > 0:
        if isla[strk][stlb - 1] == 0:
            fill(strk, stlb - 1)

    return

def layer(matrix, n):
    new = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < n:
                new[i].append(0)
            else:
                new[i].append(1)
    return new

def layers(island):
    new = []
    for i in range(min_value(island) + 1, max_value(island) + 1):
        new.append(layer(island, i))
    return new

def layer_volume(layer):
    volume = 0
    wide = len(layer[0])
    tall = len(layer)
    global isla
    isla = copy.deepcopy(layer)
    
    #sys.setrecursionlimit(2500) # for 50x50 island
    for i in range(wide):
        if layer[0][i] == 0:
            fill(0, i)

        if layer[tall - 1][i] == 0:
            fill(tall - 1, i)

    for i in range(1, tall - 1):
        if layer[i][0] == 0:
            fill(i, 0)

        if layer[i][wide - 1] == 0:
            fill(i, wide - 1)

    for i in isla:
        for j in i:
            if j == 0:
                volume += 1

    return volume

def get_water_volume(island):
    volume = 0
    lay = layers(island)
    for layer in lay:
        volume += layer_volume(layer)
    print(volume)
    return 0

island = [[2, 3, 4, 5],
        [3, 2, 2, 4],
        [4, 2, 2, 4],
        [3, 2, 4, 3]]

get_water_volume(island)
