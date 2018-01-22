# iterative


def sum_it(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


print('The sum of 1 to 100 is', sum_it(100))

# recursive


def sum_rec(n):
    if n == 1:
        return 1
    else:
        return n + sum_rec(n-1)


print('The sum of 1 to 100 is', sum_rec(100))
