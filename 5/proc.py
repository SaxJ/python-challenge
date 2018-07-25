import pickle

file = open('banner.p', 'rb')
arr = pickle.load(file)
file.close()

for line in arr:
    s = ''
    for (c, n) in line:
        for i in range(n):
            s += c
    print(s)
