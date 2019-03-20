import re
import zipfile

current = '90052'

while True:
    path = f'./{current}.txt'
    print(f'Opening {path}')
    with open(path) as f:
        txt = f.readlines()
        print(txt)
        if re.search(r'\d+', txt[0]):
            current = re.search(r'\d+', txt[0]).group()
        else:
            break

    print('==================')

zip = zipfile.ZipFile('./channel.zip')
comments = b''
for zi in zip.infolist():
    comments += zi.comment

print(comments)
