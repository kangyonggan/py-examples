# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

import cmath

# from cmath import sqrt

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

d = b ** 2 - 4 * a * c

s1 = (-b + cmath.sqrt(d)) / (2 * a)
s2 = (-b - cmath.sqrt(d)) / (2 * a)

print('二次方程式 ax**2 + bx + c = 0 的两个跟分别是：{}，{}'.format(s1, s2))
