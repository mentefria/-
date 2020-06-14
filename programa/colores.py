from PIL import Image
import time

tic = time.time()
c = 0
gx = 180
gy = 10
y = 1
yt = 1
a = list()
foto = Image.open(r'C:\Users\Admin\Desktop\венера\programa\mapa.jpg')
tam = foto.size
f = open('datos.xls', 'w+')
esp = '\n'
frase = 'координаты каждой точки и их высоты\n'
a.append(esp)
a.append(frase)
for i in range(1, 181):
    a.append('долгота\t широта\t высота')
    a.append('\t\t')
a.append(esp)
while y < tam[1]:
    x = 1
    xt = 1
    while x < tam[0]:
        pixel = foto.getpixel((xt, yt))
        R = pixel[0]
        G = pixel[1]
        B = pixel[2]
        if abs(R - B) < 3:
            c = 0
        elif abs(R - G) < 3:
            c = 500
        elif abs(G - B) < 1:
            c = 8000
        else:
            if B > R and B > G:
                if abs(B - G) > 30:
                    c = -2000
                else:
                    if B in range(130, 145):
                        c = -1500
                    elif B in range(145, 160):
                        c = 6000
                    elif B in range(165, 185):
                        c = -1000
                    elif B in range(70, 80):
                        c = 9000
                    elif B in range(60, 70):
                        c = 10000
                    elif B < 60:
                        c = 11000
                    else:
                        c = 1000
            elif G > R and G > B:
                if abs(R - G) > 15:
                    c = -500
                else:
                    if G in range(110, 170):
                        c = 5000
                    elif G in range(70, 100):
                        c = 7000
                    else:
                        c = 1000
            elif R > G and R > B:
                if R in range(160, 200):
                    c = 1000
                elif R in range(140, 160):
                    c = 2000
                elif R in range(100, 120):
                    c = 3000
                elif R in range(80, 100):
                    c = 4000
                elif R < 70:
                    c = 12000
                else:
                    c = 2000
        s = ('%i\t %i\t %i \t\t' % (gx, gy, c))
        a.append(s)
        x = x + 86.01117318435
        xt = x - (x % 1)
        gx = gx + 2
        if gx > 360:
            gx = 2
    a.append(esp)
    y = y + 83.8
    yt = y - (y % 1)
    gy = gy - 2
f.writelines(a)
f.close()
toc = time.time()
print(toc - tic, 'segundos')
