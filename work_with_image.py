import cv2
import numpy as np

# считывание фотографии
img = cv2.imread('images/11249-tim.jpg')
newimg = cv2.resize(img, (300, 500)) # изменение параметров
newimg2 = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))#пропрционально уменьшить картинку(1эл.-ширина, 2эл.-высота)
img = cv2.GaussianBlur(img, (9, 9), 0) # размытие фото
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # изменение формата из RGB
img = cv2.Canny(img, 30, 30) # бинарная картинка (указание порогов)

kernel = np.ones((5, 5), np.uint8) # создание матрицы (все элементы со значением 1)
img = cv2.dilate(img, kernel, iterations=1) # изменение обводки
# kernel-количество точек за счет которых описывается изменение обводки (очерчение контуров), необходимо создать матрицу

img = cv2.erode(img, kernel, iterations=1) # уменьшение обводки (очерчения)

cv2.imshow('result', newimg2) # 2 параметра: название и переменная
cv2.imshow('result2', img[0:100, 0:150]) #обрезание фото
cv2.imshow('result', img)

print(img.shape) # в выводе: 1 элемент-высота, 2 элемент-ширина, 3 элемент-количество слоев
cv2.waitKey(0)

