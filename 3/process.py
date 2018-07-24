import re
smalls = []
# regex would be better, but eh
with open('clue.in') as f:
    for line in f:
        found = re.search(r'([a-z]+[A-Z]{3}[a-z][A-Z]{3}[a-z]+)', line)
        if found:
            s = found.group(0)
            x = re.search(r'([A-Z]{3}[a-z][A-Z]{3})', s)
            print(s)
            smalls.append(x.group(0)[3])

print(''.join(smalls))
