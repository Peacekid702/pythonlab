def counting_zero(n):
    p = 0
    for i in range(len(n)):
        if n[i] == 0:
            p += 1
            return p

n = list()
for i in range(10):
    n.append(int(input()))

print(counting_zero(n))