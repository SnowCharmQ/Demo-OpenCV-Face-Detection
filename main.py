import cv2 as cv


def demo(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    face = face_detect.detectMultiScale(gray_img)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)

cap = cv.VideoCapture(0)
cap.read()

while True:
    flag, frame = cap.read()
    if not flag:
        break
    demo(frame)
    if ord('q') == cv.waitKey(1):
        break

cv.destroyAllWindows()
