def num_len1(num):
    num = str(num)
    res = 0
    for i in num:
        res += 1
    return res


def num_len2(num):
    num = str(num)
    res = 0
    while res < len(num):
        res += 1
    return res


N = int(input())
print(num_len1(N))
print(num_len2(N))
