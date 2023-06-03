import cv2 as cv
img = cv.imread("dedy.png")
cv.imshow("Ini gambar", img)
cv.waitKey(0)
cv.destroyAllWindows()