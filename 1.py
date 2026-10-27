pi = 0
for i in range(1, 1000001):
    pi += 4 * ((-1) ** (i + 1) / (2 * i - 1))
    if i % 100000 == 0:
        print(pi)