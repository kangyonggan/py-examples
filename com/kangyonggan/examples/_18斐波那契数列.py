def fbnq(num):
    a, b = 0, 1
    print('{},{}'.format(a, b), end='')
    for i in range(3, num + 1):
        t = a + b
        a, b = b, t
        print(',{}'.format(t), end='')

fbnq(8)