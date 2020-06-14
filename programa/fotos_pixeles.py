from PIL import Image

y = 4
yt = 4
a = list()
foto = Image.open(r'C:\Users\Admin\Desktop\венера\programa\mapa.jpg')
f = open('datos.txt', 'w+')
while y < 430:
    p = 1
    pt = 1
    while p < 15400:
        pixel = foto.getpixel((pt, yt))
        s = ('%ix %iy %i %i %i\n' % (pt, yt, pixel[0], pixel[1], pixel[2]))
        a.append(s)
        p = p + 85.533333
        pt = p - (p % 1)
    y = y + 84.8
    yt = y - (y % 1)
f.writelines(a)
f.close()
