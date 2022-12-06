def steps(n):
    for i in range(1, n + 1):
        l = ''
        for j in range(1, i + 1):
            l = l + str(j)
        for j in range(i - 1, 0, -1):
            l = l + str(j)
        print(l)
    return 'End'

n = 0
n = int(input())

print(steps(n))