from PIL import Image

MOD = 24

im = Image.open("image.jpg")
size = list(im.size)
im2 = Image.new("RGB", (im.size))

x = size[0]//MOD
y = size[1]//MOD

for a in range(x):
    for b in range(y):
        lower = a * MOD
        upper = lower + MOD
        pixels = []
        for c in range(lower, upper):
            l = b * MOD
            u = l + MOD
            for d in range(l, u):
                pixels.append(im.getpixel((c,d)))
        Red = []
        Green = []
        Blue = []
        for pixel in pixels:
            RGB = list(pixel)
            Red.append(pixel[0])
            Green.append(pixel[1])
            Blue.append(pixel[2])
        Red.sort()
        Green.sort()
        Blue.sort()
        center = len(Red)//2
        temp = [Red[center], Green[center], Blue[center]]
        color = tuple(temp)
        for e in range(lower, upper):
            for f in range (l, u):
                im2.putpixel((e,f), color)

im2.save("newimage.jpg")
