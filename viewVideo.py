import cv2
# membaca video dari file
cap = cv2.VideoCapture(0)
# loop untuk membaca setiap frame video
while True:
# membaca frame video
    ret, frame = cap.read()
    # menampilkan frame video dalam jendela
    cv2.imshow('Video', frame)
# tunggu tombol keyboard ditekan dan kemudian lanjutkan ke frame berikutnya
    if cv2.waitKey(1) & 0xFF == ord('q'): #tombol q untuk menutup kamera
        break
# tutup jendela dan lepaskan memori
cap.release()
cv2.destroyAllWindows()