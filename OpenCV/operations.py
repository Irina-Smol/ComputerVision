import cv2
import numpy as np

image = cv2.imread('images/11249-tim.jpg')
image2 = np.zeros(image.shape[:2], dtype='uint8')  # создание пустого полотна по размерам фото (длина и ширина)
#img = np.zeros((350, 350), dtype='uint8')

circle = cv2.circle(image2.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(image2.copy(), (25, 25), (250, 350), 255, -1)

img1 = cv2.bitwise_and(circle, square)  # метод находит одинаковые части изображений и отображает их
img2 = cv2.bitwise_or(circle, square)  # полное соединение двух изображений
img3 = cv2.bitwise_xor(circle, square)  # объединение двух объектов, совпадающие элементы вырезаны
img4 = cv2.bitwise_not(circle)  # инверсия (вырезается элемент, остается его след противоположного цвета)

image2 = cv2.bitwise_and(image, image, mask=circle)  # использование масок (вырезание определенных частей)
image2 = cv2.bitwise_and(image, image, mask=square)

cv2.imshow('result', circle)
cv2.imshow('result2', square)
cv2.imshow('result3', img1)
cv2.imshow('result4', img2)
cv2.imshow('result5', img3)
cv2.imshow('result6', img4)
cv2.imshow('result_image', image2)
cv2.waitKey(0)
