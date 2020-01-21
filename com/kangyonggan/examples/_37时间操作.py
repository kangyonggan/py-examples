import time

# 将字符串的时间转换为时间戳
a1 = "2019-5-10 23:40:00"
print(a1)

date = time.strptime(a1, '%Y-%m-%d %H:%M:%S')
print(date)

print(time.strftime('%Y-%m-%d %H:%M:%S', date))

# 转换为时间戳
print(int(time.mktime(date)))

# 获取几天前的时间
import datetime
print(datetime.datetime.now())
print(datetime.datetime.now() - datetime.timedelta(1))