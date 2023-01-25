import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread('images/13382650.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# уменьшение шума
img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)  # обнаружение краев

# обнаружение контуров
cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)

pos = None  # posation позиция номерного знака
for c in cont:  # перебор всех контуров
    approx = cv2.approxPolyDP(c, 10, True)  # найти контуры, похожие на прямоугольник (находим закрытые формы)
    if len(approx) == 4:  # отслеживание элементов, содержащих только 4 значения
        pos = approx
        break

# использование маски
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

# вырезать только номерной знак автомобиля
x, y = np.where(mask == 255)
x1, y1 = np.min(x), np.min(y)
x2, y2 = np.max(x), np.max(y)
cropp = gray[x1:x2, y1:y2]

# чтение информации с номерного знака
text = easyocr.Reader(['en'])
text = text.readtext(cropp)

# подпись
res = text[0][-2]
final_img = cv2.putText(img, res, (x1, y2 ), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
final_img = cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), 4)

pl.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
pl.show()

