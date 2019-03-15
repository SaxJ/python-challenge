import re

current = '90052'

while True:
    path = f'./{current}.txt'
    print(f'Opening {path}')
    with open(path) as f:
        txt = f.readlines()
        print(txt)
        current = re.search(r'\d+', txt[0]).group()

    print('==================')
