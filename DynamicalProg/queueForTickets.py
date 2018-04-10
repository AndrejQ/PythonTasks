times = [[945, 3583, 1191],
         [1245, 1923, 3157],
         [224, 3447, 316],
         [2188, 3104, 513],
         [557, 329, 2714],
         [1373, 1837, 2704],
         [1043, 2521, 2187],
         [600, 897, 3447],
         [430, 2231, 2523],
         [786, 1382, 1062]]

def current_time(times):
    all_times = [times[0][0],
                 min(times[0][0] + times[1][0], times[0][1]),
                 min(times[0][0] + times[1][0] + times[2][0], times[0][1] + times[2][0], times[0][0] + times[1][1], times[0][2])]
    for i in range(3, len(times)):
        all_times.append(min(
            all_times[i - 3] + times[i - 2][2],
            all_times[i - 2] + times[i - 1][1],
            all_times[i - 1] + times[i - 0][0]
        ))
    return all_times[-1]


print(current_time(times))
