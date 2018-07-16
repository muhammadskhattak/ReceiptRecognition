# import numpy as np
import cv2
import random

cap = cv2.VideoCapture(0)
color_limit = 1000
col = []
for i in range(0, color_limit):
    col.append((random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255)))
template = cv2.imread("template.jpg", 0)

while True:
    ret, frame = cap.read()
    edges = cv2.Canny(frame, 100, 70)
    cv2.imshow("Canny", edges)
    cv2.imshow("Frame", frame)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
