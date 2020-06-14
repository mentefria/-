from PIL import Image
import time

tic = time.time()
gy = 88
y = 0
a = list()
foto = Image.open(r'C:\Users\Admin\Desktop\венера\programa\recortada.png')
tam = foto.size
dx = tam[0] / 179
dy = tam[1] / 89
f = open('datos_3.xls', 'w+')
a.append('\n')
a.append('координаты каждой точки и их высоты\n')
for i in range(1, 181):
    a.append('долгота\t широта\t высота\t\t')
a.append('\n')
while y < tam[1]:
    gx = -120
    x = 0
    while x < tam[0]:
        pixel = foto.getpixel((int(x), int(y)))
        R = pixel[0]
        G = pixel[1]
        B = pixel[2]
        if abs(R - G) < 10:
            c = 2000
        else:
            if B >= G and B > R:
                if B > 180:
                    c = -2000
                elif abs(B - G) > 40:
                    c = -3000
                else:
                    c = -1000
            elif G > R and G > B:
                if G > 190:
                    c = 1000
                elif G > 140:
                    c = 0
                else:
                    c = -500
            elif R > B and R > G:
                if R < 200:
                    if R > 190:
                        c = 8000
                    elif R > 180:
                        c = 9000
                    elif R > 170:
                        c = 10000
                    else:
                        c = 11000
                else:
                    if G > 175:
                        c = 3000
                    elif G > 150:
                        c = 4000
                    elif G > 100:
                        c = 5000
                    else:
                        c = 6000
            else:
                print('error en %ix %iy' % (int(x), int(y)))
                print(pixel)
        s = ('%i\t %i\t %i \t\t' % (gx, gy, c))
        a.append(s)
        x += dx
        gx += 2
        if gx == 182:
            gx = -178

    a.append('\n')
    y += dy
    gy -= 2
f.writelines(a)
f.close()
toc = time.time()
print(toc - tic, 'segundos')
