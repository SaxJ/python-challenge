import re
import zipfile

current = '90052'
zip = zipfile.ZipFile('./channel.zip')
comments = ''

while True:
    path = f'./{current}.txt'
    with open(path) as f:
        txt = f.readlines()
        comments += zip.getinfo(f'{current}.txt').comment.decode('utf-8')
        if re.search(r'\d+', txt[0]):
            current = re.search(r'\d+', txt[0]).group()
        else:
            break

print(comments)
