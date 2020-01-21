test_str = "kangyonggan.com"
print(test_str)

# 移除字符串中的指定位置字符
new_str = test_str.replace(test_str[3], "", 1)
print(new_str)

# 判断字符串是否存在子字符串
print(test_str.find('ong'))
print(test_str.find('o1ng'))
if 'ong' in test_str:
    print('存在')
else:
    print('不存在')

# 长度
print(len(test_str))

# 将字符串作为代码执行
exec('print(max(1, 2))')

# 字符串翻转
print(test_str[::-1])