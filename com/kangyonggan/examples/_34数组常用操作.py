# 定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
# 例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
# 以下演示了将数组的前面两个元素放到数组后面。
#
# 原始数组:
# [1, 2, 3, 4, 5, 6, 7]
# 翻转后：
# [3, 4, 5, 6, 7, 1, 2]

arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)

num = 2
left = arr[0:num]
print(left)

right = arr[num:]
print(right)

right.extend(left)
print(right)

# 翻转数组
arr.reverse()
print(arr)

# 查找元素
print(arr.index(2))

# 复制数组
arr2 = arr[:]
print(arr2)

# 清空数组
arr2.clear()
print(arr2)

# 计算元素在列表中出现的次数
print(arr.count(2))

# 求和
print(sum(arr))

# min
print(min(arr))