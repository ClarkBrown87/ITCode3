def sum_evens1(n):
    sum_res = 0
    for num in range(1, n+1):
        if num % 2 == 0:
            sum_res += num
    return sum_res


def sum_evens2(n):
    sum_res = 0
    num = 1
    while num <= n:
        if num % 2 == 0:
            sum_res += num
        num += 1
    return sum_res


N = int(input())
print(sum_evens1(N))
print(sum_evens2(N))
