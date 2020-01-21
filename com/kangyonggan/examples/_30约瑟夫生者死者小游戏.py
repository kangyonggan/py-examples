# 30 个人在一条船上，超载，需要 15 人下船。
# 于是人们排成一队，排队的位置即为他们的编号。
# 报数，从 1 开始，数到 9 的人下船。
# 如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？

peoples = []
for i in range(1, 31):
    peoples.append(i)

print(peoples)

index = 0
while len(peoples) > 15:
    target = (8 + index) % len(peoples)
    print(peoples[target], '号下船, 此时target=', target)
    del peoples[target]
    index = target
    print(peoples, len(peoples))

