list = [int(i) for i in input().split(' ')]

max = max(list)
min = min(list)

for i in range(len(list)):
    if list[i] == max:
        list[i] = min
    elif list[i] == min:
        list[i] = max
print(list)