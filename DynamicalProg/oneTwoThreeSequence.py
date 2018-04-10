"""
сколько последовательностей состоящих из 1 2 3, в которых 1 не соседствует с другой 1
"""
def recursive_n(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    else:
        return 2 * recursive_n(n - 1) + 2 * recursive_n(n - 2)


def linear_n(n):
    if n == 0:
        return 0
    nums = [1, 3]
    for i in range(2, n + 1):
        nums.append(2 * nums[i - 1] + 2 * nums[i - 2])
    return nums[-1]


print(linear_n(2))
