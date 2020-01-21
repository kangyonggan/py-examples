# 排序
arr = [{"name": "Taobao", "age": 100},
       {"name": "Runoob", "age": 7},
       {"name": "Google", "age": 100},
       {"name": "Wiki", "age": 200}]
print(arr)

print(sorted(arr, key=lambda item: item['age']))
print(sorted(arr, key=lambda item: item['age'], reverse=True))

# 遍历字典
dict = {'a': 100, 'b': 200, 'c': 300}
for i in dict:
    print(i)
    print(dict[i])

# 移除字典点键值(key/value)对
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
print(test_dict)

del test_dict['Google']
print(test_dict)

# 弹出
item = test_dict.pop('Taobao')
print(item)
print(test_dict)

# 合并
dict1 = {'a': 10, 'b': 8}
dict2 = {'a': 5, 'd': 6, 'c': 4}

dict1.update(dict2)
print(dict1)
print(dict2)

dict1 = {'a': 10, 'b': 8}
dict2 = {'a': 5, 'd': 6, 'c': 4}
dict3 = {**dict1, **dict2}
print(dict1)
print(dict2)
print(dict3)
