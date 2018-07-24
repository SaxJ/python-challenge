counts = {}

with open('mess.in') as f:
    for line in f:
        for c in line:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

print(counts)
