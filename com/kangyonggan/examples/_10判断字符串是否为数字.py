# 判断是否为数字
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        for i in n:
            unicodedata.numeric(i)
        return True
    except ValueError:
        return False


print('{}'.format(is_number('3')))
print('{}'.format(is_number('0.4')))
print('{}'.format(is_number('0.4f')))
print('{}'.format(is_number('4e-2')))
print('{}'.format(is_number('4asd')))
print('{}'.format(is_number('四')))
print('{}'.format(is_number('八十')))
