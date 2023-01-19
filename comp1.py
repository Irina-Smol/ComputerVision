import cv2

# считывание фотографии
img = cv2.imread('images/11249-tim.jpg')
cv2.imshow('result', img) # 2 параметра: название и переменная
cv2.waitKey(0)

# считывание видео
cap = cv2.VideoCapture('videos/Infograph_line_and_top_point_on_black_screen.mp4')
while True:
    success, img2 = cap.read()
    cv2.imshow('result2', img2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# считывание с видеокамеры 
cap2 = cv2.VideoCapture(0)
cap2.set(3, 500) # ширина(id = 3)
cap2.set(4, 300)  # высота(id = 4)

while True:
    success, img3 = cap2.read()
    cv2.imshow('result3', img3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break