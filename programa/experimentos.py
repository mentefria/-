import xlwt
from PIL import Image

a = 12
f = xlwt.Workbook()
f2 = f.add_sheet("Prueba")
f2.write(0,0,'putazorra')
f.save("prueba.xls")
foto = Image.open(r'C:\Users\Admin\Desktop\венера\programa\mapa.jpg')
tam = foto.size
print(abs(-2))
print(tam[0] / 180)
print(foto.format, foto.size, foto.mode)
if a > 200:
    c = 1
elif a > 190:
    c = 2
elif a > 180:
    c = 3
else:
    c = 4
print('c = ', c)