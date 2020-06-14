from PIL import Image
import time

tic = time.time()
gx = 180
gy = 10
y = 4
yt = 4
a = list()
foto = Image.open(r'C:\Users\Admin\Desktop\венера\programa\mapa.jpg')
f = open('datos.xls', 'w+')
esp = ('\n')
a.append(esp)
a.append(esp)
a.append(esp)
while y < 430:
    p = 1
    pt = 1
    while p < 15400:
        pixel = foto.getpixel((pt, yt))
        s = ('%ix\t %iy\t %i\t %i\t %i\t\t' % (gx, gy, pixel[0], pixel[1], pixel[2]))
        a.append(s)
        p = p + 85.533333
        pt = p - (p % 1)
        gx = gx + 2
        if gx > 360:
            gx = 0
    a.append(esp)
    y = y + 84.8
    yt = y - (y % 1)
    gy = gy - 2
f.writelines(a)
f.close()
toc = time.time()
print(toc - tic, 'segundos')
