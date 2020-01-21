def hcf(x, y):
    small = min(x, y)
    hcf = 1
    for i in range(2, small + 1):
        if x % i ==0 and y % i == 0:
            hcf = i

    return hcf

print('{}和{}的最大公约数为:{}'.format(2, 2, hcf(2, 2)))
print('{}和{}的最大公约数为:{}'.format(2, 3, hcf(2, 3)))
print('{}和{}的最大公约数为:{}'.format(2, 4, hcf(2, 4)))
print('{}和{}的最大公约数为:{}'.format(4, 6, hcf(4, 6)))
print('{}和{}的最大公约数为:{}'.format(12, 6, hcf(12, 6)))
print('{}和{}的最大公约数为:{}'.format(5, 9, hcf(5, 9)))