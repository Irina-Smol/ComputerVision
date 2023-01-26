import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8') # матрица (все элементы = 0)

# RGB - стандарт
# BGR - формат в OpenCV
#photo[:] = 255, 0, 0   синий по максимуму, а зеленого и красного не добавлено, все изображение
#photo[100:150, 200:280] = 119, 201, 105 # окраска небольшой части фото

cv2.rectangle(photo, (50, 70), (100, 100), (119, 201, 105), thickness=3) # обводка квадрата
# если указать thickness=cv2.FILLED , то будет полная заливка квадрата
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[1] // 2), (119, 201, 105), thickness=3)
# линия в середине по всей ширине фото
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[1] // 2), 50, (119, 201, 105), thickness=10)
# 50-радиус
cv2.putText(photo, 'Iriska', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), thickness=3)

cv2.imshow('photo', photo)
cv2.waitKey(0)
