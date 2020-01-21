def factorial(num):
    if num < 0:
        print('负数没有阶乘')
    elif num == 0:
        return 1
    else:
        r = 1
        for i in range(1, num + 1):
            r *= i
        return r

print('{}'.format(factorial(5)))
