def factorial_n(N):
    factor = 1
    for i in range(1, N+1):
        print(i)
        factor *= i
        print(factor, "\n")

    return factor


N = int(input())
factor = factorial_n(N)