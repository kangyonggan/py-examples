a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

p = (a + b + c) / 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print('三角形面积为：{}'.format(s))
