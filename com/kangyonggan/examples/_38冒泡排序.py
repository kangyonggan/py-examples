def bubbleSort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d\t" % arr[i], end=''),
