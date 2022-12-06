set = [int(i) for i in input().split()]
l = list()
for i in range(1, len(set)):
    if set[i] > set[i - 1]:
        l.append(set[i])
print(" ".join(str(i) for i in l))
