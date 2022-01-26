def rec(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return rec(n // 2) + rec(n - 1)
    else:
        return rec(n - 1)


print(rec(16))
