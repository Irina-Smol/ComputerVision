import cv2
import numpy as np

img = cv2.imread('images/11249-tim.jpg')
img1 = cv2.flip(img, 0) # отзеркаливание картинки по вертикали
img2 = cv2.flip(img, 1) # отзеркаливание по горизонтали
img3 = cv2.flip(img, -1) # отзеркаливание по вертикали и горизонтали

# вращение картинки
def rotate(img_param, angle):
    height, width = img.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1) # матрица вращения
    return cv2.warpAffine(img_param, mat, (width, height))

img4 = rotate(img, 90)

# смещение фото
def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]]) # в матрице каждый элемент типа float
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))

img5 = transform(img, 30, 200)

# контуры изображения
img6 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # серое изображение
img6 = cv2.GaussianBlur(img, (5, 5), 0)   # размытие фото (нечетные числа)
img6 = cv2.Canny(img, 100, 140)  # числа ниже 100-черный, выше 140-белый

# con -контуры, hir -иерархия объектов(порядок)
con, hir = cv2.findContours(img6, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(con) # координаты точек контуров

new_img = np.zeros(img.shape, dtype='uint8') # создание полотна
cv2.drawContours(new_img, con, -1, (230, 111, 148), 2) # рисование новой картинки по контурам

cv2.imshow('result1', img1)
cv2.imshow('result2', img2)
cv2.imshow('result3', img3)
cv2.imshow('result4', img4)
cv2.imshow('result5', img5)
cv2.imshow('result6', img6)
cv2.imshow('result_new', new_img)

cv2.waitKey(0)