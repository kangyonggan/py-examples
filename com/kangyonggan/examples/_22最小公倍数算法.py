def lcm(x, y):
    small = min(x, y)
    hcf = 1
    for i in range(2, small + 1):
        if x % i ==0 and y % i == 0:
            hcf = i

    return x * y / hcf

print('{}和{}的最小公倍数为:{}'.format(2, 2, lcm(2, 2)))
print('{}和{}的最小公倍数为:{}'.format(2, 3, lcm(2, 3)))
print('{}和{}的最小公倍数为:{}'.format(2, 4, lcm(2, 4)))
print('{}和{}的最小公倍数为:{}'.format(4, 6, lcm(4, 6)))
print('{}和{}的最小公倍数为:{}'.format(12, 6, lcm(12, 6)))
print('{}和{}的最小公倍数为:{}'.format(5, 9, lcm(5, 9)))