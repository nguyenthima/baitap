list = [3,54,6,7,8,9]
lenth = len(list)
for i in range(0, lenth - 1):
    for j in range(i + 1, lenth):
        if (list[i] > list[j]):
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp
print(list)