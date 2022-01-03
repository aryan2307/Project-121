import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

time.sleep(2)
bg = 0
image = cv2.imread("bangkok.jpg")

while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    i = cv2.resize(img, (640, 480))
    j = cv2.resize(image, (640, 480))
    u_black = np.array([104, 143, 70])
    l_black = np.array([30, 30, 0])
    mask = cv2.inRange(img, l_black, u_black)
    result = cv2.bitwise_and(img, img, mask = mask)
    f = i - result
    f = np.where(f == 0, j, f)
    cv2.imshow("mask", f)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()