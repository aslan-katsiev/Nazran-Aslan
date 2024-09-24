from PIL import Image

image = Image.open('image.png')
pixels = image.load()
x, y = image.size

min_x, min_y, max_x, max_y = (x - 1, y - 1, 0, 0)

for i in range(x):
    for j in range(y):
        if pixels[i, j] != pixels[0, 0]:
            if min_x > i:
                min_x = i
            if min_y > j:
                min_y = j
            if max_x < i:
                max_x = i
            if max_y < j:
                max_y = j

im = image.crop((min_x, min_y, max_x, max_y))
im.save('res.png')