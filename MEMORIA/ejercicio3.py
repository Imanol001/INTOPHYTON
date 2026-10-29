b = 0
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]

for a in range(10):
    if c[a] % 2 == 0:
        b += c[a]

print(b)
