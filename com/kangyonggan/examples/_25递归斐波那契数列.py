def recur_fibo(n):
    if n <= 2:
        return n - 1
    else:
        return recur_fibo(n - 2) + recur_fibo(n - 1)


for i in range(1, 20):
    print(recur_fibo(i), ' ', end='')
