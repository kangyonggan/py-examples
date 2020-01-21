import time

print('计时开始：')

while True:
    start = time.time()
    try:
        while True:
            print('计时：', round(time.time() - start, 0))
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        print('总共耗时:', round(time.time() - start, 2))
        break
