def isarmnum(num):
    sum, temp, n = 0, num, len(str(num))
    while temp:
        p = temp % 10
        sum += p ** n
        temp //= 10

    return sum == num

for i in range(1000):
    if isarmnum(i):
        print('{}'.format(i))

