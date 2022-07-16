import cv2
img = cv2.cvtColor(cv2.imread("img_closed.png"), cv2.COLOR_BGR2GRAY)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(img,
                                    scaleFactor=1.1,
                                    minNeighbors=5)
eye_list = []
for (x, y, w, h) in eyes:
    eye = img[y:y + h, x:x + w]
    eye_list.append(eye)

img_blur_1 = cv2.GaussianBlur(eye_list[0],
                              (5, 5),
                              0)
img_blur_2 = cv2.GaussianBlur(eye_list[1],
                              (5, 5),
                              0)
edge_1 = cv2.Canny(image=img_blur_1,
                   threshold1=100,
                   threshold2=250)
edge_2 = cv2.Canny(image=img_blur_2,
                   threshold1=100,
                   threshold2=250)

cv2.imshow("edge_1", edge_1)
cv2.imshow("edge_2", edge_2)

cv2.waitKey(0)
cv2.destroyWindow()
