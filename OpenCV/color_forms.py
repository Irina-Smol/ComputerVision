import cv2

img = cv2.imread('images/11249-tim.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # конвертация изображения к формату HSV
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # конвертация изображения к формату LAB

img3 = cv2.cvtColor(img2, cv2.COLOR_LAB2BGR)
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img4)  # разделение на слои

img5 = cv2.merge([r, g, b])  # объединение слоев (картинка искажена от первоначальной)
img6 = cv2.merge([b, g, r])  # картинка такая же, как первоначальная

cv2.imshow('result1', img1)
cv2.imshow('result2', img2)
cv2.imshow('result3', img3)
cv2.imshow('result4', img4)
cv2.imshow('result_layer', r)
cv2.imshow('result5', img5)
cv2.imshow('result6', img6)
cv2.waitKey(0)
