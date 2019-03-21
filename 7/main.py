from PIL import Image

im = Image.open('oxygen.png')
pixels = im.load()
vals = []
for x in range(3, 610, 7):
    vals.append(pixels[x, 45][0])

print(vals)
print(''.join([chr(x) for x in vals]))
print(''.join([chr(x) for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]]))
