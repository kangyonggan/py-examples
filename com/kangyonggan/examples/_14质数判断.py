def isprime(num):
    if num <= 3:
        return True
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
    return True


for i in range(20):
    print('{}--->{}'.format(i, isprime(i)))
