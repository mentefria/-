from PIL import Image
import os

a = list()
q = 0
foto = Image.open(r'C:\Users\Admin\Desktop\венера\programa\RED.jpg')
datos = list(foto.getdata())
pixel = foto.getpixel((0, 0))
foto.close()
f = open('datos.txt', 'w+')
while q < 150:
    q = q + 84
    for i in range(0, 37):
        s = ('%i %i %i %i\n' % (q, datos[84 * i][0], datos[84 * i][1], datos[84 * i][2]))
        a.append(s)
f.writelines(a)
f.close()
